# CTF — Overview (Conditional Token Framework)

Source:
https://docs.polymarket.com/developers/CTF/overview

---

## Description

The Conditional Token Framework (CTF) is the on-chain system used by Polymarket
to create, split, merge, and redeem conditional tokens.

CTF enables prediction markets by representing outcomes as ERC-1155 tokens
whose value depends on the resolution of a condition.

---

## Core Concepts

### Condition

A condition represents a real-world question with multiple possible outcomes.

- Each condition has a unique conditionId.
- Conditions are resolved by an oracle.
- Once resolved, only the winning outcome token can be redeemed.

---

### Outcome Slots

- Each condition has one or more outcome slots.
- Each slot corresponds to a possible outcome.
- Outcome slots are indexed starting from 0.

---

### Conditional Tokens

- Implemented using the ERC-1155 standard.
- Each outcome token represents a claim on collateral if that outcome resolves.
- Tokens are transferable and composable.

---

## Lifecycle Overview

1. A condition is created.
2. Collateral tokens are split into outcome tokens.
3. Outcome tokens can be traded.
4. The condition is resolved by an oracle.
5. Winning outcome tokens are redeemed for collateral.

---

## Key Contracts

- ConditionalTokens
  Core smart contract implementing the CTF logic.

- Oracle / Adapter Contracts
  Responsible for reporting condition resolution.

---

## Use Cases

- Binary prediction markets (YES / NO)
- Multi-outcome markets
- Composability with DeFi protocols

---

## Notes

- CTF operations are on-chain and require gas.
- Most higher-level Polymarket features ultimately map to CTF primitives.