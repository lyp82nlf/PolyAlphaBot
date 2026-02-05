# Data API — Core — Get Top Holders For Markets

Source:
https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets

---

## Description

Returns the top holders for one or more markets.

This endpoint provides information about the largest position holders in
specified markets, useful for analyzing market concentration and liquidity.

---

## HTTP Request

Method:
GET

Path:
 /data/markets/top-holders

---

## Authentication

No authentication required.

---

## Query Parameters

- market (string, optional)
  Market ID.
  When provided, returns top holders for this market.

- asset_id (string, optional)
  Asset token ID to filter holders.

- limit (integer, optional)
  Maximum number of holders to return per market.

---

## Response

The response is an array of holder objects.

### Holder Object Fields

- wallet_address (string)
  Wallet address of the holder.

- market_id (string)
  Market identifier.

- asset_id (string)
  Token ID of the position.

- outcome (string)
  Outcome associated with the position (YES / NO).

- size (string)
  Position size held by the wallet.

---

## Example Response

[
  {
    "wallet_address": "0xabc123...",
    "market_id": "market_123",
    "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
    "outcome": "YES",
    "size": "250"
  },
  {
    "wallet_address": "0xdef456...",
    "market_id": "market_123",
    "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
    "outcome": "YES",
    "size": "180"
  }
]

---

## Notes

- Returns only aggregated holding data.
- Does not expose private user information beyond wallet address.
- Useful for transparency and market analysis.