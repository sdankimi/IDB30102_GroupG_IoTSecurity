# IDB30102 Group G – IoT Security Research Project

## Design and Evaluation of a Lightweight Authentication Protocol for Resource-Constrained Internet of Things Devices

---

## Group Information

**Group:** Group G

**Programme:** Bachelor of Cybersecurity Technology with Honours

### Group Members

| Name | Student ID |
|---|---|
| [AHMAD DANISH HAKIMI BIN AHMAD JUNAIDI DOINIL JALALAINI] | [52215226431] |
| [IZZAT IRSYADUDDIN BIN ARSHAD] | [52215226022] |
| [ALIMIE MUSTAQIM BIN MAZUDI] | [52215226059] |
| [WAN MUSTAQIM BIN WAN MOHD AZIZI] | [52215226174] |
| [ZARUL AMAR HAFIDZ BIN SHAHARUDIN] | [52215226021] |

---

## Assigned Research Area

**Internet of Things (IoT) Security and Device Authentication**

The research focuses on authentication mechanisms for resource-constrained IoT devices, with particular attention to security, computational efficiency, communication overhead, energy consumption, and resistance to common network attacks.

---

## Research Problem

Resource-constrained IoT devices have limited processing power, memory, and battery capacity. Strong authentication mechanisms may introduce high computational overhead, latency, and energy consumption.

In addition, lightweight authentication mechanisms may not always integrate physical or contextual verification, which can increase exposure to threats such as:

- Spoofing
- Device impersonation
- Replay attacks
- Man-in-the-Middle (MITM) attacks

---

## Research Aim

To design, implement, and evaluate a lightweight device authentication protocol for resource-constrained IoT environments while maintaining strong security and minimizing computational and communication overhead.

---

## Research Objectives

1. To analyze the security vulnerabilities and efficiency gaps in current IoT authentication mechanisms through a systematic literature review.

2. To design and construct a lightweight authentication protocol incorporating efficient cryptographic primitives for resource-constrained IoT nodes.

3. To evaluate the performance and security resilience of the proposed protocol against existing baseline schemes in terms of latency, energy consumption, and resistance to common network attacks.

---

## Proposed Solution

The proposed research investigates a lightweight IoT authentication mechanism using efficient authentication techniques suitable for resource-constrained devices.

The preliminary proof-of-concept currently includes:

- Device identification
- Random nonce generation
- Timestamp freshness verification
- HMAC-SHA256 authentication
- Replay detection
- RSSI-based physical/context verification
- Authentication acceptance or rejection
- Preliminary latency and communication-overhead measurements

The final research is expected to evaluate the mechanism on resource-constrained IoT devices such as ESP32 and Raspberry Pi Pico.

---

## Research Methodology

**Research Methodology:** Design Science Research Methodology (DSRM)

The research follows the main Design Science Research stages:

1. Problem identification
2. Definition of solution objectives
3. Design and development
4. Demonstration
5. Evaluation
6. Communication

DSRM was selected because the research involves designing, developing, demonstrating, and evaluating a technical IoT security artifact.

### Development Model

**Prototyping Model**

The proposed authentication mechanism will be developed initially as a preliminary software prototype before being refined and evaluated using resource-constrained IoT hardware.

---

## Proposed System Architecture

The preliminary architecture consists of:

```text
Resource-Constrained IoT Device
        |
        | Device ID
        | Nonce
        | Timestamp
        | HMAC-SHA256
        | RSSI
        v
Authentication Server
        |
        | Verify Device ID
        | Verify Timestamp
        | Check Nonce / Replay
        | Verify HMAC
        | Verify RSSI Range
        v
Authentication Decision
        |
        +---- ACCEPT
        |
        +---- REJECT
        |
        v
Results and Evaluation
