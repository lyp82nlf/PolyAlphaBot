# Pricing — Get Market Price

Source:
https://docs.polymarket.com/api-reference/pricing/get-market-price

---

## Description

Returns the current market price for a given asset.

This endpoint provides the latest traded or implied price for the specified
token in the Polymarket CLOB.

---

## HTTP Request

Method:
GET

Path:
 /pricing/market-price/{asset_id}

---

## Path Parameters

- asset_id (string, required)
  The token ID of the asset whose market price is requested.

---

## Response

The response contains the current market price for the asset.

### Response Fields

- asset_id (string)
  Token ID of the asset.

- price (string)
  Current market price.

- timestamp (string)
  Unix timestamp (milliseconds) when the price was calculated.

---

## Example Response

{
  "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
  "price": "0.57",
  "timestamp": "1672290701000"
}

---

## Notes

- price is returned as a string.
- timestamp is in milliseconds.
- This endpoint returns a snapshot, not historical data.