# Data API — Core — Get User Activity

Source:
https://docs.polymarket.com/api-reference/core/get-user-activity

---

## Description

Returns recent activity for a specific user.

User activity includes actions such as trades, position changes, and other
account-related events, aggregated into a single activity feed.

---

## HTTP Request

Method:
GET

Path:
 /data/users/{wallet_address}/activity

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
  Maximum number of activity records to return.

- cursor (string, optional)
  Cursor for pagination.

---

## Response

The response is an array of activity objects.

### Activity Object Fields

- id (string)
  Unique identifier of the activity record.

- type (string)
  Type of activity (e.g. trade, position_update).

- market_id (string, optional)
  Associated market ID, if applicable.

- asset_id (string, optional)
  Associated asset ID, if applicable.

- outcome (string, optional)
  Outcome related to the activity.

- side (string, optional)
  BUY or SELL (for trade-related activity).

- price (string, optional)
  Price associated with the activity.

- size (string, optional)
  Size associated with the activity.

- timestamp (string)
  Unix timestamp (milliseconds) when the activity occurred.

---

## Example Response

[
  {
    "id": "activity_123",
    "type": "trade",
    "market_id": "market_123",
    "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
    "outcome": "YES",
    "side": "BUY",
    "price": "0.57",
    "size": "10",
    "timestamp": "1672610000000"
  }
]

---

## Pagination

- When more activity records are available, a cursor is returned.
- Use the cursor parameter to retrieve subsequent pages.

---

## Notes

- This endpoint aggregates multiple activity types into a single feed.
- Useful for user dashboards and activity timelines.