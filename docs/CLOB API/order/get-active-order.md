# CLOB Orders — Get Active Order

Source:
https://docs.polymarket.com/developers/CLOB/orders/get-active-order

---

## Description

Returns all active (open) orders for the authenticated user.

This endpoint is used to retrieve orders that are currently open and have not
been fully filled or cancelled.

---

## HTTP Request

Method:
GET

Path:
 /orders/active

---

## Authentication

This endpoint requires authentication.
The returned orders are scoped to the authenticated user.

---

## Response

The response is an array of active order objects.

### Active Order Object Fields

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
  Order status (typically OPEN or PARTIALLY_FILLED).

- timestamp (string)
  Unix timestamp (milliseconds) when the order was created.

- last_update (string)
  Unix timestamp (milliseconds) when the order was last updated.

---

## Example Response

[
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
  },
  {
    "id": "0xabc...",
    "asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",
    "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
    "side": "SELL",
    "outcome": "NO",
    "price": "0.49",
    "size": "8",
    "size_matched": "0",
    "status": "OPEN",
    "timestamp": "1672290703000",
    "last_update": "1672290703000"
  }
]

---

## Notes

- Only orders that are not fully filled or cancelled are returned.
- Fully FILLED or CANCELLED orders will not appear in this list.
- For historical orders, use get-order or trades endpoints.