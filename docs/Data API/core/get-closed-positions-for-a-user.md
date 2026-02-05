# Data API — Core — Get Closed Positions For A User

Source:
https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user

---

## Description

Returns closed (settled) positions for a specific user.

Closed positions are positions that have been fully resolved or exited and are
no longer active.

---

## HTTP Request

Method:
GET

Path:
 /data/positions/closed/{wallet_address}

---

## Authentication

No authentication required.

---

## Path Parameters

- wallet_address (string, required)
  Blockchain wallet address of the user.

---

## Query Parameters

- market (string, optional)
  Filter closed positions by market ID.

- limit (integer, optional)
  Maximum number of closed positions to return.

- cursor (string, optional)
  Cursor for pagination.

---

## Response

The response is an array of closed position objects.

### Closed Position Object Fields

- market_id (string)
  Identifier of the market.

- asset_id (string)
  Token ID representing the position.

- outcome (string)
  Outcome associated with the position.

- size (string)
  Position size.

- average_price (string)
  Average entry price.

- exit_price (string)
  Exit or settlement price.

- realized_pnl (string)
  Realized profit or loss.

- closed_at (string)
  Unix timestamp (milliseconds) when the position was closed.

---

## Example Response

[
  {
    "market_id": "market_123",
    "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
    "outcome": "YES",
    "size": "10",
    "average_price": "0.55",
    "exit_price": "1.00",
    "realized_pnl": "4.50",
    "closed_at": "1672630000000"
  }
]

---

## Pagination

- When more closed positions are available, a cursor is returned.
- Use the cursor parameter to retrieve additional pages.

---

## Notes

- Only settled or fully exited positions appear here.
- Useful for PnL analysis and trading history review.