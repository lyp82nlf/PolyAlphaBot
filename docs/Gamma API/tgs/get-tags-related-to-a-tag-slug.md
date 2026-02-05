# Gamma API — Tags — Get Tags Related To A Tag (By Tag Slug)

Source:
https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug

---

## Description

Returns tags that are related to a given tag, identified by tag slug.

This endpoint is the slug-based equivalent of
"get-tags-related-to-a-tag-id" and returns full tag objects.

---

## HTTP Request

Method:
GET

Path:
 /tags/slug/{slug}/related

---

## Authentication

No authentication required.

---

## Path Parameters

- slug (string, required)
  URL-friendly identifier of the tag.

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

- Returned structure is identical to the ID-based related tags endpoint.
- Slug-based lookup is typically used in URL-driven applications.