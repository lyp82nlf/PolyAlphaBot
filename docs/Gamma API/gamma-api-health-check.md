# Gamma API — Health Check

Source:
https://docs.polymarket.com/api-reference/gamma-status/gamma-api-health-check

---

## Description

Health check endpoint for the Gamma API.

This endpoint can be used to verify that the Gamma API service is up and
responding to requests.

---

## HTTP Request

Method:
GET

Path:
 /gamma/health

---

## Authentication

No authentication required.

---

## Response

The response indicates the current status of the Gamma API.

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

- This endpoint is intended for monitoring and uptime checks.
- A successful response indicates that the Gamma API is operational.