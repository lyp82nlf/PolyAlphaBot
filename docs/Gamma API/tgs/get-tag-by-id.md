# Gamma API — Tags — Get Tag By ID

Source:
https://docs.polymarket.com/api-reference/tags/get-tag-by-id

---

## Description

Returns detailed information for a single tag identified by its ID.

This endpoint is used to fetch metadata for a specific tag.

---

## HTTP Request

Method:
GET

Path:
 /tags/{id}

---

## Authentication

No authentication required.

---

## Path Parameters

- id (string, required)
  Unique identifier of the tag.

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

- Tag IDs are stable identifiers used across the Gamma API.
- This endpoint returns a single tag object, not an array.