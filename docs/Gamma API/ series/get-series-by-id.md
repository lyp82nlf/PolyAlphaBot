# Gamma API — Series — Get Series By ID

Source:
https://docs.polymarket.com/api-reference/series/get-series-by-id

---

## Description

Returns detailed information for a single series identified by its ID.

This endpoint provides full metadata for a series, including descriptive
information and associated tags.

---

## HTTP Request

Method:
GET

Path:
 /series/{id}

---

## Authentication

No authentication required.

---

## Path Parameters

- id (string, required)
  Unique identifier of the series.

---

## Response

The response is a series object.

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

---

## Notes

- This endpoint returns a single series object.
- Use it to fetch full series details when navigating from a list view.