# Data API — Core — Get Trader Leaderboard Rankings

Source:
https://docs.polymarket.com/api-reference/core/get-trader-leaderboard-rankings

---

## Description

Returns trader leaderboard rankings.

This endpoint provides ranking data for traders based on performance metrics
such as volume or profit, depending on the leaderboard configuration.

---

## HTTP Request

Method:
GET

Path:
 /data/leaderboard/traders

---

## Authentication

No authentication required.

---

## Query Parameters

- timeframe (string, optional)
  Time window for the leaderboard (e.g. daily, weekly, all_time).

- limit (integer, optional)
  Maximum number of traders to return.

---

## Response

The response is an array of leaderboard entry objects.

### Leaderboard Entry Fields

- rank (integer)
  Rank position on the leaderboard.

- wallet_address (string)
  Trader wallet address.

- username (string, optional)
  Display name of the trader, if available.

- metric_value (string)
  Value of the metric used for ranking (e.g. volume, pnl).

---

## Example Response

[
  {
    "rank": 1,
    "wallet_address": "0xabc123...",
    "username": "top_trader",
    "metric_value": "15432.50"
  },
  {
    "rank": 2,
    "wallet_address": "0xdef456...",
    "username": "second_best",
    "metric_value": "14320.10"
  }
]

---

## Notes

- Metric definitions depend on the leaderboard type.
- Rankings are read-only and publicly accessible.