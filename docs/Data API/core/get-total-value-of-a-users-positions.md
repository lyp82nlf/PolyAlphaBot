# Data API — Core — Get Total Value Of A User's Positions

Source:
https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions

---

## Description

Returns the total value of all positions held by a specific user.

This endpoint aggregates the current value of a user's open positions across
all markets, providing a high-level portfolio valuation.

---

## HTTP Request

Method:
GET

Path:
 /data/users/{wallet_address}/positions/value

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

The response is a summary object representing total position value.

### Response Fields

- total_value (string)
  Total current value of the user's positions.

- total_unrealized_pnl (string)
  Total unrealized profit or loss across all positions.

- updated_at (string)
  Unix timestamp (milliseconds) when the valuation was last updated.

---

## Example Response

{
  "total_value": "1250.45",
  "total_unrealized_pnl": "32.10",
  "updated_at": "1672620000000"
}

---

## Notes

- Only open (non-settled) positions are included.
- This endpoint is typically used for portfolio summary views.