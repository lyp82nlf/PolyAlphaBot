# Proxy Wallet — Overview

Source:
https://docs.polymarket.com/developers/proxy-wallet

---

## Description

The Proxy Wallet is a smart-contract-based wallet used by Polymarket to
abstract on-chain complexity for users.

It allows users to trade, split, merge, and redeem conditional tokens without
directly managing every on-chain transaction themselves.

---

## Purpose

- Improve UX by reducing the need for users to interact directly with contracts.
- Enable gas abstraction and meta-transactions.
- Act as a programmable execution layer for user actions.

---

## Key Characteristics

- Each user is associated with a Proxy Wallet.
- The Proxy Wallet executes transactions on behalf of the user.
- Permissions are controlled and scoped to approved actions.

---

## Core Capabilities

- Execute CTF operations (split, merge, redeem).
- Interact with the CLOB contracts.
- Support gasless or relayed transactions (via builders / relayers).

---

## Architecture Overview

User → Off-chain API / Relayer → Proxy Wallet → On-chain Contracts

The Proxy Wallet:
- Receives signed instructions.
- Executes validated actions.
- Maintains isolation between users.

---

## Security Model

- Actions must be explicitly authorized.
- Proxy Wallet logic restricts callable functions.
- Users do not expose private keys to the backend.

---

## Use Cases

- Gasless trading
- Batched operations
- Safer user interaction with CTF primitives

---

## Notes

- Proxy Wallets are a critical abstraction layer in Polymarket.
- Most users never interact with Proxy Wallets directly.