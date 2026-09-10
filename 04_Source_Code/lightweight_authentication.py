import hashlib
import hmac
import json
import secrets
import time
from dataclasses import dataclass


def _canonical_message(packet: dict) -> bytes:
    """Return the fields protected by HMAC in a stable byte format."""
    protected = {
        "device_id": packet["device_id"],
        "nonce": packet["nonce"],
        "timestamp": packet["timestamp"],
        "rssi": packet["rssi"],
    }
    return json.dumps(protected, sort_keys=True, separators=(",", ":")).encode()


def packet_size_bytes(packet: dict) -> int:
    """Approximate application-layer message size as UTF-8 JSON bytes."""
    return len(json.dumps(packet, sort_keys=True, separators=(",", ":")).encode())


@dataclass
class AuthResult:
    accepted: bool
    reason: str


class IoTDevice:
    """Simplified resource-constrained IoT device."""

    def __init__(self, device_id: str, shared_key: bytes):
        self.device_id = device_id
        self.shared_key = shared_key

    def create_authentication_packet(self, rssi: int) -> dict:
        """
        Create a fresh authentication request.

        rssi is a simple physical-layer/context signal in dBm.
        Example values: -45 (strong), -70 (weaker).
        """
        packet = {
            "device_id": self.device_id,
            "nonce": secrets.token_hex(16),
            "timestamp": int(time.time()),
            "rssi": int(rssi),
        }

        packet["auth_tag"] = hmac.new(
            self.shared_key,
            _canonical_message(packet),
            hashlib.sha256,
        ).hexdigest()

        return packet


class AuthenticationServer:
    """
    Simplified authentication server.

    It checks:
    1. registered device identity
    2. timestamp freshness
    3. nonce replay
    4. HMAC-SHA256 integrity/authenticity
    5. RSSI plausibility against an enrolled baseline
    """

    def __init__(self, freshness_window_seconds: int = 10):
        self.devices = {}
        self.used_nonces = set()
        self.freshness_window_seconds = freshness_window_seconds

    def register_device(
        self,
        device_id: str,
        shared_key: bytes,
        baseline_rssi: int,
        rssi_tolerance: int = 12,
    ) -> None:
        self.devices[device_id] = {
            "shared_key": shared_key,
            "baseline_rssi": int(baseline_rssi),
            "rssi_tolerance": int(rssi_tolerance),
        }

    def verify(self, packet: dict) -> AuthResult:
        required = {"device_id", "nonce", "timestamp", "rssi", "auth_tag"}
        if not required.issubset(packet):
            return AuthResult(False, "missing required field")

        device_id = packet["device_id"]

        if device_id not in self.devices:
            return AuthResult(False, "unknown device")

        # Freshness check
        now = int(time.time())
        age = abs(now - int(packet["timestamp"]))
        if age > self.freshness_window_seconds:
            return AuthResult(False, "stale timestamp")

        # Replay check
        nonce_id = (device_id, packet["nonce"])
        if nonce_id in self.used_nonces:
            return AuthResult(False, "replay detected")

        profile = self.devices[device_id]

        # Cryptographic authentication + integrity check
        expected_tag = hmac.new(
            profile["shared_key"],
            _canonical_message(packet),
            hashlib.sha256,
        ).hexdigest()

        if not hmac.compare_digest(expected_tag, packet["auth_tag"]):
            return AuthResult(False, "invalid authentication tag")

        # Simplified physical-layer/context verification using RSSI
        lower = profile["baseline_rssi"] - profile["rssi_tolerance"]
        upper = profile["baseline_rssi"] + profile["rssi_tolerance"]

        if not lower <= int(packet["rssi"]) <= upper:
            return AuthResult(False, "RSSI outside enrolled range")

        # Mark nonce as used only after all checks succeed
        self.used_nonces.add(nonce_id)
        return AuthResult(True, "device authenticated")


def demo():
    shared_key = secrets.token_bytes(32)

    device = IoTDevice("ESP32_01", shared_key)

    server = AuthenticationServer()
    server.register_device(
        device_id="ESP32_01",
        shared_key=shared_key,
        baseline_rssi=-50,
        rssi_tolerance=12,
    )

    packet = device.create_authentication_packet(rssi=-54)
    result = server.verify(packet)

    print("LIGHTWEIGHT IoT AUTHENTICATION DEMO")
    print("-----------------------------------")
    print(f"Device ID       : {packet['device_id']}")
    print(f"Nonce           : {packet['nonce']}")
    print(f"Timestamp       : {packet['timestamp']}")
    print(f"RSSI            : {packet['rssi']} dBm")
    print(f"Message size    : {packet_size_bytes(packet)} bytes")
    print(f"Result          : {'ACCEPTED' if result.accepted else 'REJECTED'}")
    print(f"Reason          : {result.reason}")


if __name__ == "__main__":
    demo()
