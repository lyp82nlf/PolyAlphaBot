# Builder — Examples

Source:
https://docs.polymarket.com/developers/builders/examples

---

## Description

Provides example workflows and usage patterns for builders integrating with
Polymarket.

These examples illustrate how builders typically combine attribution,
relayers, proxy wallets, and CLOB / CTF operations.

---

## Example Use Cases

### 1. Trading Bot

- Bot evaluates market conditions.
- Bot creates attributed orders with a builder_id.
- Orders are submitted via a relayer.
- Trades are executed through the Proxy Wallet.
- Volume is attributed to the builder.

---

### 2. Custom Frontend

- User interacts with a custom UI.
- UI prepares and signs order requests.
- Builder attribution metadata is attached.
- Relayer submits the request.
- Execution occurs on-chain via Proxy Wallet.

---

### 3. Analytics or Automation Tool

- Tool monitors markets or events.
- Automatically places or adjusts orders.
- Uses builder attribution for tracking impact.
- Relies on relayers for execution.

---

## Typical Components in Examples

- Builder ID
- Signed payloads
- Relayer endpoints
- Proxy Wallet execution
- Attribution verification

---

## Common Patterns

- Always include builder_id when placing orders.
- Validate attribution in test environments.
- Handle relayer failures and retries gracefully.

---

## Notes

- Examples are illustrative, not exhaustive.
- Exact APIs, SDKs, and flows may evolve over time.