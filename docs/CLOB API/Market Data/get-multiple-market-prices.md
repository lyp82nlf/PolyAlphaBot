# Pricing — Get Multiple Market Prices

Source:
https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices

---

## Description

Returns the current market prices for multiple assets.

This endpoint allows clients to fetch prices for a list of token IDs in a single
request.

---

## HTTP Request

Method:
GET

Path:
 /pricing/market-prices

---

## Query Parameters

- asset_ids (array of strings, required)
  List of asset token IDs.

---

## Response

The response contains an array of market price objects.

### Market Price Object

- asset_id (string)
  Token ID of the asset.

- price (string)
  Current market price.

- timestamp (string)
  Unix timestamp (milliseconds) when the price was calculated.

---

## Example Request (Query)

?asset_ids=ASSET_ID_1&asset_ids=ASSET_ID_2

---

## Example Response

[
  {
    "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
    "price": "0.57",
    "timestamp": "1672290701000"
  },
  {
    "asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",
    "price": "0.49",
    "timestamp": "1672290701000"
  }
]

---

## Notes

- asset_ids are provided as repeated query parameters.
- All prices are returned as strings.
- This endpoint returns a snapshot of current prices.