# Data API — Core — Get Trades For A User Or Markets

Source:
https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets

---

## Description

Returns historical trades for a specific user or for specific markets.

This endpoint provides executed trade data that can be filtered by user wallet
address, market ID, or both.

---

## HTTP Request

Method:
GET

Path:
 /data/trades

---

## Authentication

No authentication required.

---

## Query Parameters

- user (string, optional)
  Wallet address of the user.
  When provided, returns trades executed by this user.

- market (string, optional)
  Market ID.
  When provided, returns trades for this market.

- asset_id (string, optional)
  Asset token ID to filter trades.

- limit (integer, optional)
  Maximum number of trades to return.

- cursor (string, optional)
  Cursor for pagination.

---

## Response

The response is an array of trade objects.

### Trade Object Fields

- trade_id (string)
  Unique identifier of the trade.

- market_id (string)
  Market identifier.

- asset_id (string)
  Token ID of the traded asset.

- outcome (string)
  Outcome associated with the trade (YES / NO).

- side (string)
  BUY or SELL.

- price (string)
  Execution price.

- size (string)
  Trade size.

- timestamp (string)
  Unix timestamp (milliseconds) when the trade occurred.

---

## Example Response

[
  {
    "trade_id": "trade_123",
    "market_id": "market_123",
    "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
    "outcome": "YES",
    "side": "BUY",
    "price": "0.57",
    "size": "10",
    "timestamp": "1672605000000"
  }
]

---

## Pagination

- When more trades are available, a cursor is returned.
- Use the cursor parameter to retrieve subsequent pages.

---

## Notes

- This endpoint returns **historical trade data**.
- It is commonly used for trade history views and analytics.
- For real-time trades, use the CLOB WebSocket user-channel.