import copy
import secrets

from lightweight_authentication import AuthenticationServer, IoTDevice


def show(name, result):
    status = "PASS" if result.accepted else "BLOCKED"
    print(f"{name:<30} -> {status}: {result.reason}")


def main():
    legitimate_key = secrets.token_bytes(32)
    wrong_key = secrets.token_bytes(32)

    server = AuthenticationServer()
    server.register_device(
        "ESP32_01",
        legitimate_key,
        baseline_rssi=-50,
        rssi_tolerance=12,
    )

    device = IoTDevice("ESP32_01", legitimate_key)

    print("ATTACK / SECURITY TESTS")
    print("-----------------------")

    # 1. Normal authentication
    valid_packet = device.create_authentication_packet(rssi=-52)
    show("Legitimate authentication", server.verify(valid_packet))

    # 2. Replay attack: resend exactly the same accepted packet
    show("Replay attack", server.verify(valid_packet))

    # 3. Impersonation: attacker claims ESP32_01 but does not know the key
    attacker = IoTDevice("ESP32_01", wrong_key)
    forged_packet = attacker.create_authentication_packet(rssi=-51)
    show("Impersonation attack", server.verify(forged_packet))

    # 4. Message modification / MITM-style tampering:
    # change RSSI after the legitimate HMAC was generated
    tamper_packet = device.create_authentication_packet(rssi=-50)
    tamper_packet["rssi"] = -30
    show("Message tampering", server.verify(tamper_packet))

    # 5. Physical/context mismatch:
    # valid cryptographic key, but signal is far outside enrolled RSSI range
    physical_mismatch = device.create_authentication_packet(rssi=-88)
    show("Physical RSSI mismatch", server.verify(physical_mismatch))


if __name__ == "__main__":
    main()
