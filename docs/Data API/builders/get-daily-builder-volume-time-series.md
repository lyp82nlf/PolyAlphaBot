# Data API — Builders — Get Daily Builder Volume Time Series

Source:
https://docs.polymarket.com/api-reference/builders/get-daily-builder-volume-time-series

---

## Description

Returns daily volume time-series data for a specific builder.

This endpoint provides historical daily trading volume attributed to a builder,
allowing analysis of growth and activity trends over time.

---

## HTTP Request

Method:
GET

Path:
 /data/builders/{builder_id}/volume/daily

---

## Authentication

No authentication required.

---

## Path Parameters

- builder_id (string, required)
  Unique identifier of the builder.

---

## Query Parameters

- start_time (string, optional)
  Start timestamp (Unix milliseconds) for the time range.

- end_time (string, optional)
  End timestamp (Unix milliseconds) for the time range.

---

## Response

The response is an array of daily volume data points.

### Daily Volume Data Point Fields

- date (string)
  Date for the data point (ISO date string).

- volume (string)
  Total trading volume attributed to the builder on that date.

---

## Example Response

[
  {
    "date": "2024-01-01",
    "volume": "12345.67"
  },
  {
    "date": "2024-01-02",
    "volume": "15678.90"
  }
]

---

## Notes

- Volume is aggregated per calendar day.
- Useful for tracking builder performance trends over time.