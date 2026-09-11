# Proposed Architecture and Flowchart

This folder contains the proposed architecture and authentication process flow for the lightweight IoT authentication protocol.

## Proposed System Architecture

The proposed system consists of a resource-constrained IoT device and an authentication server.

The IoT device generates authentication information including:

- Device ID
- Random nonce
- Timestamp
- HMAC-SHA256 authentication value
- RSSI value for preliminary physical/context verification

The authentication server verifies the device identity, timestamp freshness, nonce, authentication value, and RSSI range before accepting or rejecting the authentication request.

## Authentication Process Flow

The authentication process performs several verification stages:

1. Device registration check
2. Timestamp freshness check
3. Replay detection using the nonce
4. HMAC-SHA256 verification
5. RSSI range verification
6. Authentication decision

The diagrams in this folder are consistent with the proposed methodology and preliminary source code of the research project.
