# Gamma API — Events — Get Event By Slug

Source:
https://docs.polymarket.com/api-reference/events/get-event-by-slug

---

## Description

Returns detailed information for a single event identified by its slug.

This endpoint is functionally equivalent to "get-event-by-id", but uses the
event slug instead of the event ID.

---

## HTTP Request

Method:
GET

Path:
 /events/slug/{slug}

---

## Authentication

No authentication required.

---

## Path Parameters

- slug (string, required)
  URL-friendly identifier of the event.

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

- Returned object schema is identical to get-event-by-id.
- Slug-based lookup is commonly used in routing and SEO-friendly URLs.