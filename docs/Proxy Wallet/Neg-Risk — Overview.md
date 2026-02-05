# Neg-Risk — Overview

Source:
https://docs.polymarket.com/developers/neg-risk/overview

---

## Description

Neg-Risk (Negative Risk) is a mechanism used by Polymarket to manage markets
where the maximum downside risk is capped or reduced.

It enables special market structures where losses can be limited, often
used in certain political or structured markets.

---

## Purpose

- Reduce user downside risk in specific market types.
- Enable more flexible market designs.
- Improve capital efficiency for certain prediction markets.

---

## Core Concept

Neg-Risk markets adjust how collateral and payouts are handled so that
participants are not exposed to unlimited or full collateral loss.

Instead, the maximum loss is predefined by market rules.

---

## How It Works (High Level)

1. A Neg-Risk market is created with special parameters.
2. Trades are executed through adapted contracts.
3. Risk exposure is capped according to the Neg-Risk configuration.
4. Settlement respects the capped loss rules.

---

## Relationship to CTF

- Neg-Risk builds on top of the Conditional Token Framework.
- It modifies how conditional tokens are split, merged, or settled.
- Special adapter contracts are used to enforce Neg-Risk logic.

---

## Key Components

- Neg-Risk Adapter
  Smart contract layer that applies Neg-Risk rules.

- ConditionalTokens
  Base framework used underneath Neg-Risk markets.

---

## Use Cases

- Political markets with asymmetric payouts.
- Markets where user losses must be strictly bounded.
- Advanced market structures beyond simple YES/NO.

---

## Notes

- Neg-Risk markets require specialized handling.
- Not all Polymarket markets use Neg-Risk.
- Developers should explicitly detect Neg-Risk markets before interacting.