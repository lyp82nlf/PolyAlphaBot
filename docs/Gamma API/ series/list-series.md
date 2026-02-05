# Gamma API — Series — List Series

Source:
https://docs.polymarket.com/api-reference/series/list-series

---

## Description

Returns a list of series available in the Gamma API.

A series represents a collection of related events or markets that are grouped
together under a common theme or timeline.

---

## HTTP Request

Method:
GET

Path:
 /series

---

## Authentication

No authentication required.

---

## Query Parameters

- event (string, optional)
  Filter series by event ID.

- sport (string, optional)
  Filter series by sport.

- league (string, optional)
  Filter series by league.

- tag (string, optional)
  Filter series by tag ID or slug.

- limit (integer, optional)
  Maximum number of series to return.

- cursor (string, optional)
  Cursor for pagination.

---

## Response

The response is an array of series objects.

### Series Object Fields

- id (string)
  Unique identifier of the series.

- title (string)
  Human-readable title of the series.

- slug (string)
  URL-friendly identifier for the series.

- description (string)
  Description of the series.

- tags (array)
  Array of tags associated with the series.

- status (string)
  Current status of the series.

- start_time (string)
  Scheduled start time (Unix timestamp, milliseconds).

- end_time (string)
  Scheduled end time (Unix timestamp, milliseconds).

---

## Example Response

[
  {
    "id": "series_123",
    "title": "2024 NBA Playoffs",
    "slug": "2024-nba-playoffs",
    "description": "Markets related to the 2024 NBA Playoffs",
    "tags": ["sports", "basketball", "nba"],
    "status": "active",
    "start_time": "1672000000000",
    "end_time": "1673000000000"
  }
]

---

## Pagination

- When more series are available, a cursor is returned.
- Use the cursor parameter to retrieve additional pages.

---

## Notes

- Series are used to group events/markets at a higher level than events.
- Useful for long-running or multi-event themes.