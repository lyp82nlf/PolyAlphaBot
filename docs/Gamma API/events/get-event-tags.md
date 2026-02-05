# Gamma API — Events — Get Event Tags

Source:
https://docs.polymarket.com/api-reference/events/get-event-tags

---

## Description

Returns the tags associated with a specific event.

This endpoint is used to retrieve tag metadata linked to an event, allowing
clients to understand how the event is categorized.

---

## HTTP Request

Method:
GET

Path:
 /events/{id}/tags

---

## Authentication

No authentication required.

---

## Path Parameters

- id (string, required)
  Unique identifier of the event.

---

## Response

The response is an array of tag objects.

### Tag Object Fields

- id (string)
  Unique identifier of the tag.

- name (string)
  Human-readable tag name.

- slug (string)
  URL-friendly identifier for the tag.

- description (string)
  Description of the tag.

---

## Example Response

[
  {
    "id": "sports",
    "name": "Sports",
    "slug": "sports",
    "description": "Markets related to sporting events"
  },
  {
    "id": "basketball",
    "name": "Basketball",
    "slug": "basketball",
    "description": "Basketball-related markets"
  }
]

---

## Notes

- Tags returned here are full tag objects, not just IDs.
- This endpoint is commonly used when displaying event metadata.