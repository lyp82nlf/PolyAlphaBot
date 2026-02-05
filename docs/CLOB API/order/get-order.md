# CLOB Orders — Get Order

Source:
https://docs.polymarket.com/developers/CLOB/orders/get-order

---

## Description

Returns details for a specific order on the Polymarket CLOB.

This endpoint is used to fetch the current state and metadata of an order
by its order ID.

---

## HTTP Request

Method:
GET

Path:
 /orders/{order_id}

---

## Path Parameters

- order_id (string, required)
  Unique identifier of the order.

---

## Response

The response returns the order object.

### Response Fields

- id (string)
  Order ID.

- asset_id (string)
  Token ID of the asset.

- market (string)
  Market identifier (condition ID).

- side (string)
  BUY or SELL.

- outcome (string)
  Outcome associated with the order.

- price (string)
  Order price (present for LIMIT orders).

- size (string)
  Original order size.

- size_matched (string)
  Size that has been matched so far.

- status (string)
  Current order status (e.g. OPEN, PARTIALLY_FILLED, FILLED, CANCELLED).

- timestamp (string)
  Unix timestamp (milliseconds) when the order was created.

- last_update (string)
  Unix timestamp (milliseconds) when the order was last updated.

---

## Example Response

{
  "id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
  "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
  "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
  "side": "BUY",
  "outcome": "YES",
  "price": "0.57",
  "size": "10",
  "size_matched": "5",
  "status": "PARTIALLY_FILLED",
  "timestamp": "1672290701000",
  "last_update": "1672290712000"
}

---

## Notes

- price may be omitted for MARKET orders.
- size_matched indicates how much of the order has been filled.
- Order status can evolve over time; polling this endpoint or using the
  user-channel websocket is recommended.