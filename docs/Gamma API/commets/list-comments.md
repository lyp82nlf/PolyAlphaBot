# Gamma API — Comments — List Comments

Source:
https://docs.polymarket.com/api-reference/comments/list-comments

---

## Description

Returns a list of comments from the Gamma API.

Comments are user-generated content associated with events, markets, or users.

---

## HTTP Request

Method:
GET

Path:
 /comments

---

## Authentication

No authentication required.

---

## Query Parameters

- event (string, optional)
  Filter comments by event ID.

- market (string, optional)
  Filter comments by market ID.

- user (string, optional)
  Filter comments by user wallet address.

- limit (integer, optional)
  Maximum number of comments to return.

- cursor (string, optional)
  Cursor for pagination.

---

## Response

The response is an array of comment objects.

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

[
  {
    "id": "comment_123",
    "user": "0x1234abcd5678ef901234abcd5678ef901234abcd",
    "username": "market_trader_01",
    "content": "I think this outcome is very likely.",
    "created_at": "1672500000000",
    "updated_at": "1672500000000"
  }
]

---

## Pagination

- When more comments are available, a cursor is returned.
- Use the cursor parameter to retrieve additional pages.

---

## Notes

- Comments are public.
- Filtering by event or market is commonly used in UI comment sections.