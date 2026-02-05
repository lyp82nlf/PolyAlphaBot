# Orderbook — Get Order Book Summary

Source:
https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary

---

## Description

Returns an aggregated snapshot of the CLOB order book for a single outcome token.

The response includes bid and ask price levels with their aggregated sizes,
along with market metadata such as tick size and minimum order size.

---

## HTTP Request

Method:
GET

Path:
 /book

---

## Authentication

No authentication required.

---

## Query Parameters

- token_id (string, required)
  The outcome token ID for which to fetch the order book summary.

---

## Response

### Top-Level Fields

- market (string)
  Market condition ID associated with the token.

- asset_id (string)
  Outcome token ID.

- timestamp (string)
  ISO timestamp of the order book snapshot.

- hash (string)
  Hash representing the order book state.

- bids (array)
  Aggregated bid-side price levels.

- asks (array)
  Aggregated ask-side price levels.

- min_order_size (string)
  Minimum allowed order size for this market.

- tick_size (string)
  Minimum price increment.

- neg_risk (boolean)
  Indicates whether the market uses Neg-Risk logic.

---

### Bid / Ask Object Fields

- price (string)
  Price level.

- size (string)
  Total size available at this price.

---

## Example Response

{
  "market": "0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa",
  "asset_id": "1234567890",
  "timestamp": "2023-10-01T12:00:00Z",
  "hash": "0xabc123def456",
  "bids": [
    {
      "price": "0.57",
      "size": "120"
    }
  ],
  "asks": [
    {
      "price": "0.58",
      "size": "95"
    }
  ],
  "min_order_size": "1",
  "tick_size": "0.01",
  "neg_risk": false
}

---

## Notes

- This endpoint returns an aggregated order book snapshot.
- Individual orders are not returned.
- Used for spread calculation, depth analysis, and price discovery.
- For multiple tokens, use the multiple order book summaries endpoint.