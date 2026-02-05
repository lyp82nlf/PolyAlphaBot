# CLOB Trades — Trades

Source:
https://docs.polymarket.com/developers/CLOB/trades/trades

---

## Description

Returns trade data from the Polymarket CLOB.

This endpoint allows clients to retrieve executed trades, either scoped to
specific markets, assets, or users, depending on the provided parameters.

---

## HTTP Request

Method:
GET

Path:
 /trades

---

## Query Parameters

- market (string, optional)
  Market identifier (condition ID).
  When provided, returns trades for this market.

- asset_id (string, optional)
  Asset token ID.
  When provided, returns trades for this asset.

- owner (string, optional)
  Owner identifier.
  When provided, returns trades associated with this owner.

- limit (integer, optional)
  Maximum number of trade records to return.

- cursor (string, optional)
  Cursor for pagination.

---

## Response

The response is an array of trade objects.

### Trade Object Fields

- asset_id (string)
  Token ID of the traded asset.

- event_type (string)
  Event type. Value: "trade".

- id (string)
  Trade ID.

- market (string)
  Market identifier (condition ID).

- outcome (string)
  Outcome associated with the trade (e.g. YES, NO).

- owner (string)
  Owner identifier associated with the trade.

- price (string)
  Trade price.

- side (string)
  BUY or SELL.

- size (string)
  Trade size.

- status (string)
  Trade status.

- timestamp (string)
  Unix timestamp (milliseconds) when the trade occurred.

---

## Example Response

[
  {
    "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
    "event_type": "trade",
    "id": "28c4d2eb-bbea-40e7-a9f0-b2fdb56b2c2e",
    "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
    "outcome": "YES",
    "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
    "price": "0.57",
    "side": "BUY",
    "size": "10",
    "status": "MATCHED",
    "timestamp": "1672290701000"
  }
]

---

## Pagination

- When the number of trades exceeds the limit, a cursor is returned.
- Use the cursor parameter in subsequent requests to retrieve the next page.

---

## Notes

- This endpoint returns historical trade data.
- Results can be filtered by market, asset, or owner.
- For real-time trade updates, use the user-channel websocket.