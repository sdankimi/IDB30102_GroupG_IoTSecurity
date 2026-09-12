# Data and Sample Input

This folder contains sample input used for the preliminary lightweight IoT authentication prototype.

## sample_devices.csv

This file contains example IoT device profiles used during authentication testing.

The sample information includes:

- Device ID
- Device type
- Baseline RSSI
- RSSI tolerance

The devices represent resource-constrained IoT platforms that may be used during later physical testing.

## authentication_test_cases.csv

This file contains controlled authentication scenarios used to test the preliminary authentication mechanism.

The test cases include:

- Legitimate authentication
- Replay attack
- Impersonation attack
- Message tampering
- RSSI / physical-context mismatch

## Data Generation

The current prototype does not require a large external dataset.

Authentication values such as nonces and timestamps are generated dynamically by the Python prototype during each authentication attempt.

Future physical testing is expected to collect measurements from devices such as ESP32 and Raspberry Pi Pico.
