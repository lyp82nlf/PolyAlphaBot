# Spreads — Get Bid Ask Spreads

Source:
https://docs.polymarket.com/api-reference/spreads/get-bid-ask-spreads

---

## Description

Returns the bid-ask spread information for one or more assets.

This endpoint provides insight into market liquidity by exposing the best bid,
best ask, and spread for each requested token.

---

## HTTP Request

Method:
GET

Path:
 /spreads/bid-ask

---

## Query Parameters

- asset_ids (array of strings, required)
  List of asset token IDs.

---

## Response

The response is an array of bid-ask spread objects.

### Bid Ask Spread Object

- asset_id (string)
  Token ID of the asset.

- best_bid (string)
  Current best bid price.

- best_ask (string)
  Current best ask price.

- spread (string)
  Difference between best ask and best bid.

- timestamp (string)
  Unix timestamp (milliseconds) when the spread was calculated.

---

## Example Request (Query)

?asset_ids=ASSET_ID_1&asset_ids=ASSET_ID_2

---

## Example Response

[
  {
    "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
    "best_bid": "0.56",
    "best_ask": "0.58",
    "spread": "0.02",
    "timestamp": "1672290701000"
  },
  {
    "asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",
    "best_bid": "0.48",
    "best_ask": "0.50",
    "spread": "0.02",
    "timestamp": "1672290701000"
  }
]

---

## Notes

- All numeric values are returned as strings.
- spread is calculated as (best_ask - best_bid).
- This endpoint returns a snapshot of current spread values.
