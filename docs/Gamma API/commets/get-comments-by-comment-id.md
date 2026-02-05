# Gamma API — Comments — Get Comments By Comment ID

Source:
https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id

---

## Description

Returns a single comment identified by its comment ID.

This endpoint is used to fetch the full details of a specific comment.

---

## HTTP Request

Method:
GET

Path:
 /comments/{id}

---

## Authentication

No authentication required.

---

## Path Parameters

- id (string, required)
  Unique identifier of the comment.

---

## Response

The response is a comment object.

### Comment Object Fields

- id (string)
  Unique identifier of the comment.

- user (string)
  Wallet address of the commenter.

- username (string)
  Display name of the commenter.

- content (string)
  Text content of the comment.

- created_at (string)
  Unix timestamp (milliseconds) when the comment was created.

- updated_at (string)
  Unix timestamp (milliseconds) when the comment was last updated.

---

## Example Response

{
  "id": "comment_123",
  "user": "0x1234abcd5678ef901234abcd5678ef901234abcd",
  "username": "market_trader_01",
  "content": "I think this outcome is very likely.",
  "created_at": "1672500000000",
  "updated_at": "1672500000000"
}

---

## Notes

- This endpoint returns a single comment object.
- Use it when navigating directly to a comment or refreshing comment state.