# Gamma API — Events — List Events

Source:
https://docs.polymarket.com/api-reference/events/list-events

---

## Description

Returns a list of events available in the Gamma API.

Events represent real-world occurrences (e.g. elections, sports games)
that group together one or more markets.

---

## HTTP Request

Method:
GET

Path:
 /events

---

## Authentication

No authentication required.

---

## Query Parameters

- sport (string, optional)
  Filter events by sport.

- league (string, optional)
  Filter events by league.

- tag (string, optional)
  Filter events by tag ID or slug.

- status (string, optional)
  Filter by event status.

- limit (integer, optional)
  Maximum number of events to return.

- cursor (string, optional)
  Cursor for pagination.

---

## Response

The response is an array of event objects.

### Event Object Fields

- id (string)
  Unique identifier of the event.

- title (string)
  Human-readable title of the event.

- slug (string)
  URL-friendly identifier for the event.

- description (string)
  Description of the event.

- sport (string)
  Sport identifier.

- league (string)
  League identifier.

- tags (array)
  Array of tags associated with the event.

- status (string)
  Current status of the event.

- start_time (string)
  Scheduled start time (Unix timestamp, milliseconds).

- end_time (string)
  Scheduled end time (Unix timestamp, milliseconds).

---

## Example Response

[
  {
    "id": "event_123",
    "title": "Los Angeles Lakers vs Golden State Warriors",
    "slug": "lakers-vs-warriors",
    "description": "NBA regular season game",
    "sport": "basketball",
    "league": "nba",
    "tags": ["sports", "basketball"],
    "status": "upcoming",
    "start_time": "1672400000000",
    "end_time": "1672407200000"
  }
]

---

## Pagination

- When more events are available, a cursor is returned.
- Use the cursor parameter to fetch subsequent pages.

---

## Notes

- Events group related markets together.
- Filtering by sport, league, or tag is commonly used for browsing.