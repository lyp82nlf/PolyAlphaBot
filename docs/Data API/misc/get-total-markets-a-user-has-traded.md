# Data API — Misc — Get Total Markets A User Has Traded

Source:
https://docs.polymarket.com/api-reference/misc/get-total-markets-a-user-has-traded

---

## Description

Returns the total number of distinct markets that a user has traded in.

This endpoint aggregates trading activity to provide a count of unique markets
a user has participated in.

---

## HTTP Request

Method:
GET

Path:
 /data/users/{wallet_address}/markets/traded/count

---

## Authentication

No authentication required.

---

## Path Parameters

- wallet_address (string, required)
  Blockchain wallet address of the user.

---

## Query Parameters

None.

---

## Response

The response is a summary object.

### Response Fields

- total_markets_traded (integer)
  Number of distinct markets the user has traded in.

- updated_at (string)
  Unix timestamp (milliseconds) when the count was last updated.

---

## Example Response

{
  "total_markets_traded": 42,
  "updated_at": "1672640000000"
}

---

## Notes

- Counts unique markets only (multiple trades in the same market are counted once).
- Useful for user engagement metrics and profile statistics.