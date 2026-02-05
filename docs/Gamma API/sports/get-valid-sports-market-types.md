# Gamma API — Sports — Get Valid Sports Market Types

Source:
https://docs.polymarket.com/api-reference/sports/get-valid-sports-market-types

---

## Description

Returns the list of valid market types for sports markets.

This endpoint describes which market types are supported for each sport and
league, helping clients understand what kinds of markets can be created or
queried for sports events.

---

## HTTP Request

Method:
GET

Path:
 /sports/market-types

---

## Authentication

No authentication required.

---

## Query Parameters

None.

---

## Response

The response is an array of sport market type objects.

### Sport Market Type Object Fields

- sport (string)
  Sport identifier.

- league (string)
  League identifier.

- market_types (array of strings)
  List of supported market types for the sport/league combination.

---

## Example Response

[
  {
    "sport": "basketball",
    "league": "nba",
    "market_types": [
      "moneyline",
      "spread",
      "total"
    ]
  },
  {
    "sport": "football",
    "league": "nfl",
    "market_types": [
      "moneyline",
      "spread",
      "total"
    ]
  }
]

---

## Notes

- Market types define how outcomes are structured for sports markets.
- The set of supported market types may vary by sport and league.
- These values are typically used when filtering or creating sports markets.