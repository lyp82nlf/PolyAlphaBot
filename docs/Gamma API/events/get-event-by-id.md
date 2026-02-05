# Gamma API — Events — Get Event By ID

Source:
https://docs.polymarket.com/api-reference/events/get-event-by-id

---

## Description

Returns detailed information for a single event identified by its ID.

This endpoint provides full metadata for an event, including associated tags
and contextual information.

---

## HTTP Request

Method:
GET

Path:
 /events/{id}

---

## Authentication

No authentication required.

---

## Path Parameters

- id (string, required)
  Unique identifier of the event.

---

## Response

The response is an event object.

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

---

## Notes

- This endpoint returns a single event object.
- Use this endpoint to fetch full event details when navigating from a list view.