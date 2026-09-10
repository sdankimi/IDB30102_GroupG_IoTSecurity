import json
import secrets
import statistics
import time

from lightweight_authentication import (
    AuthenticationServer,
    IoTDevice,
    packet_size_bytes,
)


NODE_COUNTS = [1, 10, 50, 100]
TRIALS = 500


def benchmark(node_count: int):
    server = AuthenticationServer()

    devices = []
    for i in range(node_count):
        key = secrets.token_bytes(32)
        device = IoTDevice(f"ESP32_{i + 1:03d}", key)
        devices.append(device)

        server.register_device(
            device_id=device.device_id,
            shared_key=key,
            baseline_rssi=-50,
            rssi_tolerance=12,
        )

    latencies_ms = []
    sizes = []
    accepted = 0

    for i in range(TRIALS):
        device = devices[i % node_count]
        packet = device.create_authentication_packet(rssi=-52)

        start = time.perf_counter_ns()
        result = server.verify(packet)
        end = time.perf_counter_ns()

        latencies_ms.append((end - start) / 1_000_000)
        sizes.append(packet_size_bytes(packet))

        if result.accepted:
            accepted += 1

    return {
        "nodes": node_count,
        "trials": TRIALS,
        "accepted": accepted,
        "avg_latency_ms": statistics.mean(latencies_ms),
        "median_latency_ms": statistics.median(latencies_ms),
        "max_latency_ms": max(latencies_ms),
        "avg_message_bytes": statistics.mean(sizes),
    }


def main():
    print("PRELIMINARY AUTHENTICATION BENCHMARK")
    print("------------------------------------")
    print("NOTE: These are host-computer Python measurements, not ESP32 energy results.\n")

    results = []

    for nodes in NODE_COUNTS:
        result = benchmark(nodes)
        results.append(result)

        print(
            f"Nodes={result['nodes']:>3} | "
            f"Accepted={result['accepted']:>3}/{result['trials']} | "
            f"Avg latency={result['avg_latency_ms']:.6f} ms | "
            f"Median={result['median_latency_ms']:.6f} ms | "
            f"Avg payload={result['avg_message_bytes']:.1f} bytes"
        )

    with open("benchmark_results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)

    print("\nSaved results to benchmark_results.json")


if __name__ == "__main__":
    main()
