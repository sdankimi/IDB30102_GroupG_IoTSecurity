# Preliminary Source Code

This folder contains preliminary technical components for the proposed lightweight IoT device authentication research.

## Files

### `lightweight_authentication.py`
A simplified proof-of-concept authentication protocol. It uses:

- a fresh random nonce
- a timestamp freshness check
- HMAC-SHA256 for authentication and message integrity
- replay detection
- a simple RSSI range check as a preliminary physical-layer/context verification feature

The RSSI check is intentionally simple. It is not claimed to be a complete physical-layer authentication system.

### `attack_simulation.py`
Runs controlled security tests against the proof-of-concept:

- legitimate authentication
- replay attempt
- impersonation with an incorrect key
- message modification / MITM-style tampering
- physical/context mismatch using an abnormal RSSI value

### `performance_benchmark.py`
Measures preliminary software-side metrics:

- authentication latency
- message size / communication overhead
- behavior with 1, 10, 50, and 100 registered devices

The benchmark is executed on the host computer and therefore must not be presented as ESP32 or Raspberry Pi Pico energy/performance data.

## How to run

Python 3 is required. No third-party packages are needed.

Run the main demonstration:

```bash
python lightweight_authentication.py
```

Run security tests:

```bash
python attack_simulation.py
```

Run the benchmark:

```bash
python performance_benchmark.py
```

The benchmark also creates `benchmark_results.json`.

## Research alignment

This preliminary implementation supports the design and construction of a lightweight authentication protocol using efficient cryptographic primitives.

It also provides an initial way to evaluate authentication latency, communication overhead, replay resistance, impersonation resistance, and message integrity before later physical-device testing on ESP32/Raspberry Pi Pico hardware.

Future work should include actual microcontroller implementation, real energy measurements, memory measurements, packet capture, environmental variation testing, and formal verification where appropriate.
