# Pricing — Get Price History for a Traded Token

Source:
https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token

---

## Description

Returns historical price data for a traded token.

This endpoint provides time-series pricing information for an asset that has
been traded on the Polymarket CLOB.

---

## HTTP Request

Method:
GET

Path:
 /pricing/price-history/{asset_id}

---

## Path Parameters

- asset_id (string, required)
  The token ID of the traded asset.

---

## Query Parameters

- interval (string, optional)
  Time bucket size for aggregation.
  (Exact supported values are defined on the page, e.g. minute/hour/day.)

- start_time (string, optional)
  Start of the time range (Unix timestamp, milliseconds).

- end_time (string, optional)
  End of the time range (Unix timestamp, milliseconds).

---

## Response

The response is an array of historical price points.

### Price History Entry

- timestamp (string)
  Unix timestamp (milliseconds) for the data point.

- price (string)
  Price at the given timestamp.

---

## Example Response

[
  {
    "timestamp": "1672290000000",
    "price": "0.55"
  },
  {
    "timestamp": "1672290600000",
    "price": "0.56"
  },
  {
    "timestamp": "1672291200000",
    "price": "0.57"
  }
]

---

## Notes

- Prices are returned as strings.
- Only tokens with trade history will return data.
- This endpoint returns historical snapshots, not real-time updates.