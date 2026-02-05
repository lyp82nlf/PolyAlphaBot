# Gamma API — Markets — Get Market By ID

Source:
https://docs.polymarket.com/api-reference/markets/get-market-by-id

---

## Description

Returns detailed information for a single market identified by its ID.

This endpoint provides full metadata for a market, including its question,
outcomes, associated event, and current status.

---

## HTTP Request

Method:
GET

Path:
 /markets/{id}

---

## Authentication

No authentication required.

---

## Path Parameters

- id (string, required)
  Unique identifier of the market.

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

- This endpoint returns a single market object.
- Use this endpoint to fetch full market details when navigating from a list view.