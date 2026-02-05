# Gamma API — Tags — Get Tags Related To A Tag (By Tag ID)

Source:
https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-id

---

## Description

Returns tags that are related to a given tag, identified by tag ID.

Unlike the relationships endpoint, this endpoint returns full tag objects
for related tags, not just relationship metadata.

---

## HTTP Request

Method:
GET

Path:
 /tags/{id}/related

---

## Authentication

No authentication required.

---

## Path Parameters

- id (string, required)
  Unique identifier of the tag.

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
    "id": "us-politics",
    "name": "US Politics",
    "slug": "us-politics",
    "description": "Politics related to the United States"
  },
  {
    "id": "elections",
    "name": "Elections",
    "slug": "elections",
    "description": "Election-related markets"
  }
]

---

## Notes

- This endpoint returns tag details directly.
- It is useful when you need display-ready tag data.
- Relationship semantics are handled internally by Gamma.