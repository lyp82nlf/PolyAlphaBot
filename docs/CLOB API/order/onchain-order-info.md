# CLOB Orders — Onchain Order Info

Source:
https://docs.polymarket.com/developers/CLOB/orders/onchain-order-info

---

## Description

Returns on-chain information associated with a CLOB order.

This endpoint is used to retrieve blockchain-level details for an order,
such as transaction hashes and on-chain execution metadata.

---

## HTTP Request

Method:
GET

Path:
 /orders/onchain/{order_id}

---

## Path Parameters

- order_id (string, required)
  The order ID whose on-chain information is requested.

---

## Authentication

This endpoint requires authentication.
Only orders belonging to the authenticated user can be queried.

---

## Response

The response contains on-chain metadata for the specified order.

### Response Fields

- order_id (string)
  Order ID.

- tx_hash (string)
  Blockchain transaction hash associated with the order.

- block_number (string)
  Block number in which the transaction was included.

- status (string)
  On-chain status of the order execution.

- timestamp (string)
  Unix timestamp (milliseconds) when the on-chain transaction was confirmed.

---

## Example Response

{
  "order_id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
  "tx_hash": "0x9f8c3a1b2e4d5f6789abcdeffedcba9876543210",
  "block_number": "12345678",
  "status": "CONFIRMED",
  "timestamp": "1672290725000"
}

---

## Notes

- This endpoint exposes blockchain execution details, not CLOB order state.
- An order may exist off-chain before it is reflected on-chain.
- For order lifecycle status, use get-order or user-channel websocket events.