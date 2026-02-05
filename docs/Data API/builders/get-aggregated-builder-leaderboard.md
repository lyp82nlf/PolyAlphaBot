# Data API — Builders — Get Aggregated Builder Leaderboard

Source:
https://docs.polymarket.com/api-reference/builders/get-aggregated-builder-leaderboard

---

## Description

Returns aggregated leaderboard data for builders.

This endpoint provides ranking information for builders based on aggregated
metrics such as volume or activity attributed to builder integrations.

---

## HTTP Request

Method:
GET

Path:
 /data/builders/leaderboard

---

## Authentication

No authentication required.

---

## Query Parameters

- timeframe (string, optional)
  Time window for the leaderboard (e.g. daily, weekly, all_time).

- limit (integer, optional)
  Maximum number of builders to return.

---

## Response

The response is an array of builder leaderboard entries.

### Builder Leaderboard Entry Fields

- rank (integer)
  Rank position on the leaderboard.

- builder_id (string)
  Unique identifier of the builder.

- builder_name (string)
  Display name of the builder.

- metric_value (string)
  Aggregated metric value used for ranking (e.g. total volume).

---

## Example Response

[
  {
    "rank": 1,
    "builder_id": "builder_abc",
    "builder_name": "Top Builder",
    "metric_value": "245678.90"
  },
  {
    "rank": 2,
    "builder_id": "builder_xyz",
    "builder_name": "Second Builder",
    "metric_value": "198432.10"
  }
]

---

## Notes

- Metrics are aggregated across all activity attributed to each builder.
- Rankings are read-only and publicly accessible.