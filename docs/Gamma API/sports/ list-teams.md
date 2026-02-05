# Gamma API — Sports — List Teams

Source:
https://docs.polymarket.com/api-reference/sports/list-teams

---

## Description

Returns a list of sports teams supported by the Gamma API.

This endpoint provides metadata about teams that may be associated with
sports events and markets.

---

## HTTP Request

Method:
GET

Path:
 /sports/teams

---

## Authentication

No authentication required.

---

## Query Parameters

None.

---

## Response

The response is an array of team objects.

### Team Object Fields

- id (string)
  Unique identifier of the team.

- name (string)
  Human-readable team name.

- sport (string)
  Sport category the team belongs to.

- league (string)
  League the team participates in.

- slug (string)
  URL-friendly identifier for the team.

---

## Example Response

[
  {
    "id": "team_123",
    "name": "Los Angeles Lakers",
    "sport": "basketball",
    "league": "NBA",
    "slug": "los-angeles-lakers"
  },
  {
    "id": "team_456",
    "name": "New England Patriots",
    "sport": "football",
    "league": "NFL",
    "slug": "new-england-patriots"
  }
]

---

## Notes

- Team metadata is used to enrich sports events and markets.
- The exact set of teams depends on supported sports and leagues.