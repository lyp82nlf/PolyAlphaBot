# Gamma API — Tags — Get Related Tags Relationships By Tag Slug

Source:
https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-slug

---

## Description

Returns relationship information between a tag and other related tags,
identified by the tag slug.

This endpoint is equivalent to the tag-id based relationship endpoint,
but uses the tag slug instead of the tag ID.

---

## HTTP Request

Method:
GET

Path:
 /tags/slug/{slug}/relationships

---

## Authentication

No authentication required.

---

## Path Parameters

- slug (string, required)
  URL-friendly identifier of the tag.

---

## Response

The response is an array of tag relationship objects.

### Tag Relationship Object Fields

- tag_id (string)
  ID of the source tag.

- related_tag_id (string)
  ID of the related tag.

- relationship_type (string)
  Type of relationship between the tags.

---

## Example Response

[
  {
    "tag_id": "politics",
    "related_tag_id": "us-politics",
    "relationship_type": "child"
  },
  {
    "tag_id": "politics",
    "related_tag_id": "elections",
    "relationship_type": "related"
  }
]

---

## Notes

- Returned structure is identical to the ID-based relationships endpoint.
- Slug-based lookup is convenient for URL-driven applications.