# Data API — Misc — Get Open Interest History

Source:
https://docs.polymarket.com/api-reference/misc/get-open-interesthistor

---

## Description

Returns historical open interest data.

Open interest represents the total value of open positions in one or more
markets over time.

This endpoint provides time-series data that can be used to analyze liquidity
trends and market participation.

---

## HTTP Request

Method:
GET

Path:
 /data/open-interest/history

---

## Authentication

No authentication required.

---

## Query Parameters

- market (string, optional)
  Market ID.
  When provided, returns open interest history for this market.

- start_time (string, optional)
  Start timestamp (Unix milliseconds) for the time range.

- end_time (string, optional)
  End timestamp (Unix milliseconds) for the time range.

- interval (string, optional)
  Time interval for aggregation (e.g. hourly, daily).

---

## Response

The response is an array of open interest data points.

### Open Interest Data Point Fields

- timestamp (string)
  Unix timestamp (milliseconds) representing the time bucket.

- open_interest (string)
  Total open interest value at that time.

---

## Example Response

[
  {
    "timestamp": "1672500000000",
    "open_interest": "45231.75"
  },
  {
    "timestamp": "1672586400000",
    "open_interest": "47890.20"
  }
]

---

## Notes

- Open interest values are aggregated across outcomes.
- Useful for tracking liquidity growth or decline over time.
- Interval granularity affects the number of returned data points.