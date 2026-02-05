# Gamma API — Profiles — Get Public Profile By Wallet Address

Source:
https://docs.polymarket.com/api-reference/profiles/get-public-profile-by-wallet-address

---

## Description

Returns the public profile information for a user identified by a wallet address.

This endpoint exposes non-sensitive, publicly available information associated
with a Polymarket user.

---

## HTTP Request

Method:
GET

Path:
 /profiles/{wallet_address}

---

## Authentication

No authentication required.

---

## Path Parameters

- wallet_address (string, required)
  Blockchain wallet address of the user.

---

## Response

The response is a public profile object.

### Public Profile Object Fields

- wallet_address (string)
  Wallet address of the user.

- username (string)
  Display name of the user.

- avatar_url (string)
  URL to the user’s avatar image.

- bio (string)
  Short biography or description.

- joined_at (string)
  Unix timestamp (milliseconds) when the profile was created.

---

## Example Response

{
  "wallet_address": "0x1234abcd5678ef901234abcd5678ef901234abcd",
  "username": "market_trader_01",
  "avatar_url": "https://cdn.polymarket.com/avatars/market_trader_01.png",
  "bio": "Prediction market enthusiast",
  "joined_at": "1660000000000"
}

---

## Notes

- Only public information is returned.
- This endpoint does not expose private or sensitive user data.
- Useful for leaderboards, comments, and profile displays.