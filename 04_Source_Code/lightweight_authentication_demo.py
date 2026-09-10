import hashlib
import hmac
import secrets


# --------------------------------------------------
# Lightweight IoT Authentication Demonstration
# --------------------------------------------------

# Shared secret key between IoT device and server.
# In a real system, this would be securely provisioned.
SHARED_KEY = b"iot_shared_secret_key"


def generate_nonce():
    """Generate a fresh random nonce."""
    return secrets.token_hex(16)


def generate_temporary_identity(device_id, nonce):
    """
    Generate a temporary device identity using SHA-256.
    This avoids sending the real device identity directly.
    """
    data = f"{device_id}:{nonce}".encode()

    return hashlib.sha256(data).hexdigest()


def generate_authentication_code(temp_id, nonce):
    """
    Generate HMAC-SHA256 authentication value.
    """
    message = f"{temp_id}:{nonce}".encode()

    authentication_code = hmac.new(
        SHARED_KEY,
        message,
        hashlib.sha256
    ).hexdigest()

    return authentication_code


def verify_device(temp_id, nonce, received_code):
    """
    Server calculates its own HMAC and compares it
    with the value received from the IoT device.
    """

    expected_code = generate_authentication_code(
        temp_id,
        nonce
    )

    return hmac.compare_digest(
        expected_code,
        received_code
    )


# --------------------------------------------------
# Simulated IoT authentication
# --------------------------------------------------

device_id = "IoT_Device_01"

print("LIGHTWEIGHT IoT AUTHENTICATION DEMO")
print("-----------------------------------")

# Step 1: IoT device generates a nonce
nonce = generate_nonce()

print("Generated Nonce:")
print(nonce)


# Step 2: Generate temporary identity
temporary_id = generate_temporary_identity(
    device_id,
    nonce
)

print("\nTemporary Device Identity:")
print(temporary_id)


# Step 3: Generate authentication code
auth_code = generate_authentication_code(
    temporary_id,
    nonce
)

print("\nHMAC Authentication Code:")
print(auth_code)


# Step 4: Server verifies device
authenticated = verify_device(
    temporary_id,
    nonce,
    auth_code
)

print("\nAuthentication Result:")

if authenticated:
    print("SUCCESS - Device authenticated")
else:
    print("FAILED - Device rejected")
