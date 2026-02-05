# Pricing — Get Midpoint Price

Source:
https://docs.polymarket.com/api-reference/pricing/get-midpoint-price

---

## Description

Returns the midpoint price for a given asset.

The midpoint price is calculated as the average of the best bid and best ask
prices currently available in the order book.

---

## HTTP Request

Method:
GET

Path:
 /pricing/midpoint-price/{asset_id}

---

## Path Parameters

- asset_id (string, required)
  The token ID of the asset whose midpoint price is requested.

---

## Response

The response contains the midpoint price for the asset.

### Response Fields

- asset_id (string)
  Token ID of the asset.

- midpoint_price (string)
  Midpoint price calculated from the best bid and best ask.

- timestamp (string)
  Unix timestamp (milliseconds) when the midpoint was calculated.

---

## Example Response

{
  "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
  "midpoint_price": "0.575",
  "timestamp": "1672290701000"
}

---

## Notes

- midpoint_price is returned as a string.
- The value is derived from the current order book snapshot.
- If either side of the book is empty, the midpoint price may be undefined
  (behavior depends on market state).