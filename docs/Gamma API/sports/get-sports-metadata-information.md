# Gamma API — Sports — Get Sports Metadata Information

Source:
https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information

---

## Description

Returns metadata information for supported sports.

This endpoint provides high-level metadata describing each sport, which can be
used to organize teams, events, and markets.

---

## HTTP Request

Method:
GET

Path:
 /sports/metadata

---

## Authentication

No authentication required.

---

## Query Parameters

None.

---

## Response

The response is an array of sport metadata objects.

### Sport Metadata Object Fields

- id (string)
  Unique identifier of the sport.

- name (string)
  Human-readable name of the sport.

- slug (string)
  URL-friendly identifier for the sport.

- leagues (array)
  List of leagues associated with the sport.

---

## League Object Fields

- id (string)
  Unique identifier of the league.

- name (string)
  Human-readable name of the league.

- slug (string)
  URL-friendly identifier for the league.

---

## Example Response

[
  {
    "id": "basketball",
    "name": "Basketball",
    "slug": "basketball",
    "leagues": [
      {
        "id": "nba",
        "name": "NBA",
        "slug": "nba"
      },
      {
        "id": "wnba",
        "name": "WNBA",
        "slug": "wnba"
      }
    ]
  },
  {
    "id": "football",
    "name": "Football",
    "slug": "football",
    "leagues": [
      {
        "id": "nfl",
        "name": "NFL",
        "slug": "nfl"
      }
    ]
  }
]

---

## Notes

- Sports metadata provides the top-level classification for sports markets.
- Leagues are nested under each sport.
- IDs and slugs are commonly used for filtering and lookup in other endpoints.