# CLOB Orders — Create Order Batch

Source:
https://docs.polymarket.com/developers/CLOB/orders/create-order-batch

---

## Description

Creates multiple orders in a single request on the Polymarket CLOB.

This endpoint allows clients to submit a batch of orders at once, reducing
the number of HTTP calls and improving efficiency when placing many orders.

---

## HTTP Request

Method:
POST

Path:
 /orders/batch

---

## Request Body

### Request Body Structure

The request body contains an array of order objects.

- orders (array, required)
  List of orders to create.

---

## Order Object (per item)

Each order object in the batch has the same structure as a single create order
request.

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

- expiration (string, optional)
  Expiration timestamp.

- nonce (string, optional)
  Client-provided nonce for idempotency.

---

## Example Request

{
  "orders": [
    {
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
      "side": "BUY",
      "outcome": "YES",
      "price": "0.57",
      "size": "10",
      "order_type": "LIMIT"
    },
    {
      "asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",
      "side": "SELL",
      "outcome": "NO",
      "price": "0.49",
      "size": "5",
      "order_type": "LIMIT"
    }
  ]
}

---

## Response

The response contains the result of each order creation attempt.

### Response Fields

- orders (array)
  Array of created order objects.

Each returned order object includes:

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
  Order price (if applicable).

- size (string)
  Original order size.

- status (string)
  Order status.

- timestamp (string)
  Unix timestamp (milliseconds) when the order was created.

---

## Example Response

{
  "orders": [
    {
      "id": "0xaaa...",
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
      "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
      "side": "BUY",
      "outcome": "YES",
      "price": "0.57",
      "size": "10",
      "status": "OPEN",
      "timestamp": "1672290701000"
    },
    {
      "id": "0xbbb...",
      "asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",
      "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
      "side": "SELL",
      "outcome": "NO",
      "price": "0.49",
      "size": "5",
      "status": "OPEN",
      "timestamp": "1672290701000"
    }
  ]
}

---

## Notes

- Each order in the batch is processed independently.
- Some orders in the batch may succeed while others fail.
- Clients should inspect each returned order’s status.