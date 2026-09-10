import hashlib
import hmac
import secrets
import time


SHARED_KEY = b"iot_shared_secret_key"

TEST_MESSAGE = b"IoT authentication message"

ITERATIONS = 10000


def benchmark_sha256():

    start = time.perf_counter()

    for _ in range(ITERATIONS):
        hashlib.sha256(TEST_MESSAGE).digest()

    end = time.perf_counter()

    return end - start


def benchmark_hmac():

    start = time.perf_counter()

    for _ in range(ITERATIONS):

        hmac.new(
            SHARED_KEY,
            TEST_MESSAGE,
            hashlib.sha256
        ).digest()

    end = time.perf_counter()

    return end - start


def benchmark_nonce():

    start = time.perf_counter()

    for _ in range(ITERATIONS):
        secrets.token_bytes(16)

    end = time.perf_counter()

    return end - start


print("LIGHTWEIGHT AUTHENTICATION BENCHMARK")
print("------------------------------------")

print(f"Iterations: {ITERATIONS}")

sha_time = benchmark_sha256()
hmac_time = benchmark_hmac()
nonce_time = benchmark_nonce()

print("\nResults")

print(
    f"SHA-256: {sha_time:.6f} seconds"
)

print(
    f"HMAC-SHA256: {hmac_time:.6f} seconds"
)

print(
    f"Nonce Generation: {nonce_time:.6f} seconds"
)
