# Gamma API — Markets — Get Market By Slug

Source:
https://docs.polymarket.com/api-reference/markets/get-market-by-slug

---

## Description

Returns detailed information for a single market identified by its slug.

This endpoint is functionally equivalent to "get-market-by-id", but uses the
market slug instead of the market ID.

---

## HTTP Request

Method:
GET

Path:
 /markets/slug/{slug}

---

## Authentication

No authentication required.

---

## Path Parameters

- slug (string, required)
  URL-friendly identifier of the market.

---

## Response

The response is a market object.

### Market Object Fields

- id (string)
  Unique identifier of the market.

- question (string)
  Human-readable market question.

- slug (string)
  URL-friendly identifier for the market.

- description (string)
  Description of the market.

- event_id (string)
  Identifier of the parent event.

- sport (string)
  Sport identifier.

- league (string)
  League identifier.

- tags (array)
  Array of tags associated with the market.

- status (string)
  Current market status.

- outcomes (array)
  List of possible outcomes.

- start_time (string)
  Scheduled start time (Unix timestamp, milliseconds).

- end_time (string)
  Scheduled end time (Unix timestamp, milliseconds).

---

## Example Response

{
  "id": "market_123",
  "question": "Will the Lakers beat the Warriors?",
  "slug": "lakers-beat-warriors",
  "description": "NBA game outcome market",
  "event_id": "event_123",
  "sport": "basketball",
  "league": "nba",
  "tags": ["sports", "basketball"],
  "status": "open",
  "outcomes": ["YES", "NO"],
  "start_time": "1672400000000",
  "end_time": "1672407200000"
}

---

## Notes

- Returned object schema is identical to get-market-by-id.
- Slug-based lookup is commonly used in URL routing and SEO-friendly links.