# Builder — Introduction

Source:
https://docs.polymarket.com/developers/builders/builder-intro

---

## Description

The Builder program enables third-party developers to integrate with
Polymarket and receive attribution for user trading activity driven
through their applications.

Builders can create products, tools, or interfaces that route trades
to Polymarket while earning recognition and potential rewards.

---

## Purpose

- Encourage third-party ecosystem growth.
- Attribute trading volume to external integrations.
- Support relayers, bots, dashboards, and custom frontends.

---

## Core Concept

A Builder is identified by a unique builder_id.

Trades executed through a Builder-integrated flow can be attributed
to that builder for analytics, rankings, and incentive programs.

---

## Attribution Flow (High Level)

User Action
 → Builder Integration
 → Signed Request (Builder ID included)
 → Proxy Wallet / Relayer
 → On-chain Execution
 → Builder Attribution Recorded

---

## Key Benefits

- Volume attribution
- Leaderboard visibility
- Eligibility for builder incentives

---

## Typical Builder Types

- Trading bots
- Alternative frontends
- Analytics dashboards
- Automated market makers
- Relayers and execution services

---

## Notes

- Builder attribution is opt-in and explicit.
- Builders do not custody user funds.
- Builder programs may evolve over time.