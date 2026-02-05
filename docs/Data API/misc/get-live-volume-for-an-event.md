# Data API — Misc — Get Live Volume For An Event

Source:
https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event

---

## Description

Returns live trading volume for a specific event.

This endpoint provides near real-time volume data aggregated across all markets
associated with an event.

---

## HTTP Request

Method:
GET

Path:
 /data/events/{event_id}/volume/live

---

## Authentication

No authentication required.

---

## Path Parameters

- event_id (string, required)
  Unique identifier of the event.

---

## Query Parameters

None.

---

## Response

The response is a volume summary object.

### Response Fields

- event_id (string)
  Identifier of the event.

- volume (string)
  Total traded volume for the event.

- updated_at (string)
  Unix timestamp (milliseconds) when the volume was last updated.

---

## Example Response

{
  "event_id": "event_123",
  "volume": "98765.43",
  "updated_at": "1672650000000"
}

---

## Notes

- Volume is aggregated across all markets in the event.
- Intended for dashboards and real-time monitoring.