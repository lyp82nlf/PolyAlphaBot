# Data API — Health Check

Source:
https://docs.polymarket.com/api-reference/data-api-status/data-api-health-check

---

## Description

Health check endpoint for the Polymarket Data API.

This endpoint can be used to verify that the Data API service is online and
responding to requests.

---

## HTTP Request

Method:
GET

Path:
 /data/health

---

## Authentication

No authentication required.

---

## Response

The response indicates the current health status of the Data API.

### Response Fields

- status (string)
  Health status of the API.

---

## Example Response

{
  "status": "ok"
}

---

## Notes

- Intended for monitoring and uptime verification.
- Does not return any business or market data.