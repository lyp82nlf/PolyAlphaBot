# CLOB — Timeseries

Source:
https://docs.polymarket.com/developers/CLOB/timeseries

---

## Description

Provides access to time series data for CLOB markets.

This endpoint allows clients to retrieve historical metrics over time for
markets and assets, useful for analytics, charting, and backtesting.

---

## HTTP Request

Method:
GET

Path:
 /timeseries

---

## Query Parameters

- market (string, optional)
  Market identifier (condition ID).

- asset_id (string, optional)
  Asset token ID.

- metric (string, required)
  Metric to retrieve.
  (Available metrics are defined on the page.)

- interval (string, required)
  Time bucket size for aggregation.
  (Examples: minute, hour, day — exact values as defined on the page.)

- start_time (string, optional)
  Start of the time range (Unix timestamp, milliseconds).

- end_time (string, optional)
  End of the time range (Unix timestamp, milliseconds).

---

## Response

The response is an array of time series data points.

### Timeseries Entry

- timestamp (string)
  Unix timestamp (milliseconds) representing the bucket.

- value (string)
  Value of the requested metric for the given time bucket.

---

## Example Response

[
  {
    "timestamp": "1672290000000",
    "value": "123.45"
  },
  {
    "timestamp": "1672290600000",
    "value": "130.12"
  },
  {
    "timestamp": "1672291200000",
    "value": "128.90"
  }
]

---

## Notes

- All values are returned as strings.
- The meaning of `value` depends on the selected metric.
- Either market or asset_id must be provided, depending on the metric.
- This endpoint returns historical data only.