# CLOB Client — Methods (L2)

Source:
https://docs.polymarket.com/developers/CLOB/clients/methods-l2

---

## 概述

This page documents the available Level 2 (L2) methods exposed by the Polymarket
CLOB client libraries.

These methods are intended to:
- Retrieve market/orderbook related data
- Interact with pricing and market state
- Serve as client-side wrappers around CLOB REST endpoints

---

## get_order_book_summary

Description:
Returns the aggregated L2 orderbook for a given asset.

Method:
GET

Client Method:
get_order_book_summary(asset_id)

Parameters:
- asset_id (string, required)
  The token ID of the asset to fetch the orderbook for.

Returns:
Order book summary object.

---

## get_multiple_order_books_summaries

Description:
Returns aggregated L2 orderbooks for multiple assets in a single request.

Method:
POST

Client Method:
get_multiple_order_books_summaries(asset_ids)

Parameters:
- asset_ids (string[], required)
  List of asset token IDs.

Returns:
Array of order book summary objects.

---

## get_market_price

Description:
Returns the current market price for a given asset.

Method:
GET

Client Method:
get_market_price(asset_id)

Parameters:
- asset_id (string, required)
  Token ID of the asset.

Returns:
Current market price.

---

## get_multiple_market_prices

Description:
Returns current market prices for multiple assets.

Method:
GET

Client Method:
get_multiple_market_prices(asset_ids)

Parameters:
- asset_ids (string[], required)
  List of asset token IDs.

Returns:
Mapping of asset_id → price.

---

## get_midpoint_price

Description:
Returns the midpoint price for a given asset.

Method:
GET

Client Method:
get_midpoint_price(asset_id)

Parameters:
- asset_id (string, required)

Returns:
Midpoint price.

---

## get_price_history_for_traded_token

Description:
Returns historical pricing data for a traded token.

Method:
GET

Client Method:
get_price_history_for_traded_token(asset_id)

Parameters:
- asset_id (string, required)

Returns:
Time-series price history.

---

## get_bid_ask_spreads

Description:
Returns bid/ask spread information for assets.

Method:
GET

Client Method:
get_bid_ask_spreads(asset_ids)

Parameters:
- asset_ids (string[], required)

Returns:
Bid/ask spread data.

---

## get_timeseries

Description:
Returns timeseries data for markets.

Method:
GET

Client Method:
get_timeseries(...)

Parameters:
(As defined in the timeseries endpoint documentation)

Returns:
Timeseries dataset.