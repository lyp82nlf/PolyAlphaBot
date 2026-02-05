# Gamma API — Comments — Get Comments By User Address

Source:
https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address

---

## Description

Returns comments created by a specific user, identified by wallet address.

This endpoint is used to retrieve all public comments authored by a given user.

---

## HTTP Request

Method:
GET

Path:
 /comments/user/{wallet_address}

---

## Authentication

No authentication required.

---

## Path Parameters

- wallet_address (string, required)
  Blockchain wallet address of the user.

---

## Query Parameters

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
- Use the cursor parameter to retrieve subsequent pages.

---

## Notes

- Returns only public comments.
- Useful for user profile pages and activity feeds.