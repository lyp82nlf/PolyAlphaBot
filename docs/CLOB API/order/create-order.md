# CLOB Orders — Create Order

Source:
https://docs.polymarket.com/developers/CLOB/orders/create-order

---

## Description

Creates a new order on the Polymarket CLOB.

This endpoint is used to place both limit and market orders for a given asset
and outcome.

---

## HTTP Request

Method:
POST

Path:
 /orders

---

## Request Body

### Required Fields

- asset_id (string, required)
  Token ID of the asset being traded.

- side (string, required)
  Order side.
  Possible values: BUY, SELL

- outcome (string, required)
  Outcome of the market.
  Possible values depend on the market (e.g. YES, NO).

- size (string, required)
  Size of the order.
  Provided as a string.

---

### Conditional / Optional Fields

- price (string, optional)
  Price of the order.
  Required for LIMIT orders.
  Omitted for MARKET orders.

- order_type (string, optional)
  Type of order.
  Examples include LIMIT or MARKET.
  (Exact accepted values are defined on the page.)

- expiration (string, optional)
  Expiration timestamp for the order.

- nonce (string, optional)
  Client-provided nonce for idempotency.

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

The response returns information about the newly created order.

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
  Price of the order.

- size (string)
  Original order size.

- status (string)
  Current order status.

- timestamp (string)
  Unix timestamp (milliseconds) when the order was created.

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
  "status": "OPEN",
  "timestamp": "1672290701000"
}

---

## Notes

- All numeric values are returned as strings.
- price is required for LIMIT orders.
- MARKET orders do not include a price field.
- Order status may change over time and should be tracked via:
  - get-order
  - user-channel websocket