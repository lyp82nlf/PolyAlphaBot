# Gamma API — Tags — List Tags

Source:
https://docs.polymarket.com/api-reference/tags/list-tags

---

## Description

Returns a list of tags used to categorize events and markets.

Tags are used to group related markets, improve discoverability, and enable
filtering across different sections of the platform.

---

## HTTP Request

Method:
GET

Path:
 /tags

---

## Authentication

No authentication required.

---

## Query Parameters

None.

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
    "id": "politics",
    "name": "Politics",
    "slug": "politics",
    "description": "Markets related to political events"
  },
  {
    "id": "sports",
    "name": "Sports",
    "slug": "sports",
    "description": "Markets related to sporting events"
  }
]

---

## Notes

- Tags are shared across events and markets.
- Tags can be queried directly or via relationships endpoints.
- Tag IDs and slugs are commonly used as filters.