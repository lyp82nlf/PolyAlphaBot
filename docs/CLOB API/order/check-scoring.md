# CLOB Orders — Check Scoring

Source:
https://docs.polymarket.com/developers/CLOB/orders/check-scoring

---

## Description

Checks whether an order would be scored by the Polymarket CLOB scoring system.

This endpoint allows clients to simulate order scoring without actually placing
the order, helping determine if the order meets scoring requirements.

---

## HTTP Request

Method:
POST

Path:
 /orders/check-scoring

---

## Authentication

This endpoint requires authentication.

---

## Request Body

The request body contains an order definition identical to a create-order
request, but the order is not actually placed.

### Required Fields

- asset_id (string, required)
  Token ID of the asset being traded.

- side (string, required)
  BUY or SELL.

- outcome (string, required)
  Outcome of the market (e.g. YES, NO).

- size (string, required)
  Size of the order.

---

### Conditional / Optional Fields

- price (string, optional)
  Required for LIMIT orders.

- order_type (string, optional)
  Type of order (LIMIT or MARKET, as defined on the page).

---

## Example Request

{
  "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
  "side": "BUY",
  "outcome": "YES",
  "price": "0.57",
  "size": "10",
  "order_type": "LIMIT"
}

---

## Response

The response indicates whether the order would be scored.

### Response Fields

- is_scored (boolean)
  Indicates whether the order meets scoring criteria.

- reason (string, optional)
  Explanation if the order is not scored.

---

## Example Response

{
  "is_scored": true
}

---

## Notes

- This endpoint does not create an order.
- It is intended for pre-checking order eligibility for scoring.
- The scoring rules themselves are defined by Polymarket and may change.