# Gamma API — Markets — Get Market Tags By ID

Source:
https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id

---

## Description

Returns the tags associated with a specific market, identified by market ID.

This endpoint is used to retrieve tag metadata linked to a market, allowing
clients to understand how the market is categorized.

---

## HTTP Request

Method:
GET

Path:
 /markets/{id}/tags

---

## Authentication

No authentication required.

---

## Path Parameters

- id (string, required)
  Unique identifier of the market.

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
- This endpoint is commonly used when displaying market metadata.