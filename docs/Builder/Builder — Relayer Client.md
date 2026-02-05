# Builder — Relayer Client

Source:
https://docs.polymarket.com/developers/builders/relayer-client

---

## Description

The Relayer Client is a client-side or service-side component used by builders
to submit transactions to Polymarket via a relayer.

It enables gasless or abstracted transaction execution by forwarding signed
requests to relayers that execute them on-chain.

---

## Purpose

- Allow builders to submit orders without requiring users to pay gas.
- Enable off-chain signing with on-chain execution.
- Standardize interaction with Polymarket relayers.

---

## High-Level Flow

1. User or builder signs a request off-chain.
2. Builder sends the signed payload to a relayer endpoint.
3. Relayer validates the request.
4. Relayer executes the transaction via the Proxy Wallet.
5. On-chain execution occurs and attribution is recorded.

---

## Common Capabilities

- Submit CLOB orders
- Execute CTF operations (split, merge, redeem)
- Batch or sequence actions
- Attach builder attribution metadata

---

## Security Model

- Requests must be properly signed.
- Relayers validate payload integrity.
- Proxy Wallet enforces allowed execution paths.

---

## Integration Notes

- Builders typically use an official SDK or client library.
- Relayer endpoints may differ between environments.
- Error handling and retries are the responsibility of the builder.

---

## Notes

- Relayers abstract away gas and transaction submission.
- Builders should treat relayers as critical infrastructure.