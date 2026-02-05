# Gamma API — Tags — Get Related Tags Relationships By Tag ID

Source:
https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id

---

## Description

Returns relationship information between a tag and other related tags,
identified by tag ID.

This endpoint exposes how tags are related to one another within the
Gamma tagging system.

---

## HTTP Request

Method:
GET

Path:
 /tags/{id}/relationships

---

## Authentication

No authentication required.

---

## Path Parameters

- id (string, required)
  Unique identifier of the tag.

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

- Relationship types describe how tags are connected (e.g. parent, child, related).
- This endpoint returns relationships, not full tag objects.