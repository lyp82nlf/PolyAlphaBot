# CTF — Deployment Resources

Source:
https://docs.polymarket.com/developers/CTF/deployment-resources

---

## Description

Provides deployment information and on-chain resources for the
Conditional Token Framework (CTF).

This page lists contract addresses and related resources required to interact
with CTF on supported networks.

---

## Core Contracts

### ConditionalTokens

- The main smart contract implementing the Conditional Token Framework.
- Handles split, merge, and redeem operations.
- ERC-1155 compliant.

---

## Network Deployments

CTF is deployed on supported networks used by Polymarket.

Typical deployment information includes:

- Network name
- Chain ID
- ConditionalTokens contract address

(Exact addresses depend on the network and may change over time.)

---

## Related Contracts

- Oracle / Adapter Contracts  
  Used to resolve conditions and report outcomes on-chain.

- Collateral Tokens  
  ERC-20 tokens (e.g. USDC) used as collateral for conditional tokens.

---

## Developer Notes

- Always verify contract addresses against official documentation.
- Ensure correct chain ID when interacting with contracts.
- Use read-only calls to inspect conditions and positions when possible.

---

## Use Cases

- Direct on-chain interaction with CTF
- Custom integrations and tooling
- Auditing and debugging conditional token flows