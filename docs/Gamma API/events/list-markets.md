# Gamma API — Markets — List Markets

Source:
https://docs.polymarket.com/api-reference/markets/list-markets

---

## Description

Returns a list of markets available in the Gamma API.

Markets represent individual prediction markets that belong to events and
define specific outcomes users can trade on.

---

## HTTP Request

Method:
GET

Path:
 /markets

---

## Authentication

No authentication required.

---

## Query Parameters

- event (string, optional)
  Filter markets by event ID.

- sport (string, optional)
  Filter markets by sport.

- league (string, optional)
  Filter markets by league.

- tag (string, optional)
  Filter markets by tag ID or slug.

- status (string, optional)
  Filter markets by status.

- limit (integer, optional)
  Maximum number of markets to return.

- cursor (string, optional)
  Cursor for pagination.

---

## Response

The response is an array of market objects.

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

[
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
]

---

## Pagination

- When more markets are available, a cursor is returned.
- Use the cursor parameter to fetch subsequent pages.

---

## Notes

- Markets belong to events and inherit contextual metadata.
- Filtering by event or tag is common when browsing markets.