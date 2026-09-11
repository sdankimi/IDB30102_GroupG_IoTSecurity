# PART 2 : LITERATURE REVIEW
This section synthesizes research in Internet of Things (IoT) device authentication
---

## 1. Literature Review Analysis Table

The following presents five representative studies covering security approaches, their testbed, evaluation metrics, findings, and research gaps:

| Author(s) & Year | Core Focus / Objective | Dataset / Testbed | Method / Security Process | Evaluation Metrics | Key Findings | Research Limitations & Gaps |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Naif Alzahrani** *(2025)* | Lightweight D2D security for constrained networks | ProVerif simulation environment | D2D protocol using ECC and SHA-256 hashing | Energy, processing time, message size | Outperforms existing methods in battery conservation and security | Tested purely via software simulation without real hardware deployment. |
| **Deepak Kumar & Bhaskar Mondal** *(2022)* | Resistance to physical tampering and cloning | PUF circuits, Xilinx, Synopsys simulation | Physical Unclonable Function (PUF) hardware circuit verification | PUF reliability, uniqueness, energy use | Strong resistance against cloning, spoofing, and physical tampering | Temperature and voltage variations introduce noise into PUF outputs. |
| **Munkenyi Mukhandi et al.** *(2022)* | Lightweight D2D consensus authentication | Ganache/Truffle + CORE emulator (20–40 nodes) | Hashed identities in Merkle tree on permissioned blockchain | Latency (s), throughput (kb/s), CPU utilization (%) | Latency scaled near-linearly (~12–25s); faster than central MQTT | Evaluated on PC emulators; on-chain data storage and privacy unaddressed. |
| **Junqing Zhang et al.** *(2023)* | Physical-layer identification before packet decoding | Simulated RF signals | RFFI using engineered features and hybrid protocol | Physical-layer classification accuracy | Leverages unique hardware features without heavy crypto computation | RFF signatures are sensitive to environmental noise and component aging. |
| **Poornima M. Chanal & M. S. Kakkasageri** *(2023)* | Context-aware device authentication | Contextual network traffic | BDI cognitive agent combined with Random Forest ML algorithm | Context-aware prediction accuracy | Belief set explicitly models context to drive authentication decisions | Secure authentication is not fully achieved at edge/router levels. |

---

## 2. Comparison of Existing Techniques

Comparative evaluation of the primary security paradigms identified from literature research:

| Security Paradigm | Core Technology / Method | Primary Strengths | Major Limitations |
| :--- | :--- | :--- | :--- |
| **Lightweight Crypto** | ECC, ZKP, HMAC, Bitwise XOR | Reduced key size, strong mathematical security | Non-negligible bit-overhead and transmission payload size |
| **PUF & Hardware Security** | SRAM power-up states, Arbiter PUFs, BCH Fuzzy Extractors | High resistance to physical key extraction and cloning | Response sensitivity to temperature and voltage noise |
| **Blockchain & Distributed Ledgers** | Smart contracts, Merkle trees, IOTA Tangle | Eliminates single points of failure, transparent audit logs | High transaction latency, storage accumulation over time |
| **Physical Layer Security** | RF Fingerprinting (RFFI), CSI, Intelligent Reflecting Surfaces | Bypasses cryptographic key management entirely | Sensitive to physical user mobility, fast fading, and signal loss |
| **Machine Learning & AI** | Deep Neural Networks (DNN), Random Forest, Federated Learning | Context-aware, high accuracy (>97%), continuous scoring | High training/computational cost, vulnerable to noisy data |

---

## 3. Research Gap Analysis

Analysis of the literature reveals there's three overarching research gaps that are preventing existing authentication mechanisms from achieving optimal deployment efficiency in real-world IoT systems:

* **The Simulation vs. Physical Realization Disconnect:** Most current schemes rely on software verification tools (such as AVISPA, ProVerif, or Scyther) or high-level network simulators like MATLAB and NS-3. While these platforms validate mathematical logic and protocol stability, they fail to capture real-world hardware behavior—including clock skews, dynamic bus latency, memory constraints, and core power trace vulnerabilities.
* **Environmental Instability of Physical Primitives:** Hardware-assisted strategies like Physical Unclonable Functions (PUFs) and Physical Layer Authentication (PLA) eliminate the need to store keys in non-volatile memory. However, they remain highly sensitive to operating conditions. Factors like temperature fluctuations, voltage drops, and rapid device mobility introduce noise into signal outputs. Correcting this noise often requires heavy error-correction schemes (such as BCH Fuzzy Extractors) that consume significant hardware resources, offsetting their lightweight advantages.
* **Vulnerability to Post-Quantum Cryptanalysis:** The majority of modern lightweight authentication protocols depend on classical cryptography, including Elliptic Curve Cryptography (ECC) and standard SHA-256 hashing. These methods are vulnerable to emerging quantum cryptanalytic techniques. While quantum-resistant algorithms are being actively researched, their computational burden and large key sizes currently exceed what resource-constrained IoT edge devices can handle.

---

## 4. Summary of Methods and Algorithms

The cryptographic algorithms, hardware primitives, and architectural strategies identified across the literature fall into five major categories:

* **Cryptographic Primitives & Logic:** Elliptic Curve Cryptography (ECC), Zero-Knowledge Proofs (ZKP), One-Time Pads (OTP), HMAC-SHA256, symmetric-key encryption, and lightweight bitwise XOR operations.
* **Hardware-Based Primitives:** SRAM power-up state evaluations, Arbiter PUFs (APUF), and BCH Fuzzy Extractors for error mitigation.
* **Decentralized Architectures:** Permissioned Blockchains, Merkle Trees, Smart Contracts, and Directed Acyclic Graph (DAG) structures like the IOTA Tangle.
* **Physical Layer Primitives:** Radio Frequency Fingerprint Identification (RFFI), Channel State Information (CSI), Received Signal Strength (RSS), and Intelligent Reflecting Surfaces (IRS).
* **Machine Learning Architectures:** Deep Neural Networks (DNN), Random Forest classifiers, Belief-Desire-Intention (BDI) cognitive agents, and Federated Learning pipelines.

---

## 5. Relevant Datasets

The experimental environments and datasets used in existing research include:

* **Simulated Signals & Network Traffic:** Synthetic RF waveforms, AVISPA/HLPSL generated validation files, and simulated IoT packet traces.
* **Physical & Sensor Data:** Network traffic logs, IMU motion sensor datasets used for gait biometrics, and multi-modal access logs combining RFID and fingerprint data.
* **Distributed Network Testbeds:** CORE network emulators (ranging from 20 to 40 nodes), local Ethereum/Ganache blockchain environments, and localized edge servers.
* **Industrial & Contextual Logs:** Request logs from industrial access control systems, simulated Intelligent Transportation System (ITS) traffic, and distributed wireless sensor arrays.

---

## 6. Evaluation Metrics Identified from Previous Research

Researchers commonly evaluate protocol performance and feasibility using four key dimensions:

* **Computational Overhead:** Processing delay, execution time, CPU utilization, and the total count of required operations (such as hash generations, XOR calculations, or symmetric encryptions).
* **Communication Overhead:** Payload size in bytes, total message exchanges per session, and packet header bloat.
* **Resource & Energy Efficiency:** Energy consumption per authentication attempt, memory footprint (RAM and Flash usage), and impact on battery longevity.
* **Security & Classification Performance:** Overall authentication accuracy, False Positive Rate (FPR), True Positive Rate (TPR), Equal Error Rate (EER), and resilience against brute-force or physical cloning attacks.
