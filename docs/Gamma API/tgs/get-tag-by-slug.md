# Gamma API — Tags — Get Tag By Slug

Source:
https://docs.polymarket.com/api-reference/tags/get-tag-by-slug

---

## Description

Returns detailed information for a single tag identified by its slug.

This endpoint is functionally equivalent to "get-tag-by-id", but uses the
tag slug instead of the tag ID.

---

## HTTP Request

Method:
GET

Path:
 /tags/slug/{slug}

---

## Authentication

No authentication required.

---

## Path Parameters

- slug (string, required)
  URL-friendly identifier of the tag.

---

## Response

The response is a tag object.

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

{
  "id": "politics",
  "name": "Politics",
  "slug": "politics",
  "description": "Markets related to political events"
}

---

## Notes

- Tag slug is typically used in URLs and user-facing routes.
- Returned object schema is identical to get-tag-by-id.