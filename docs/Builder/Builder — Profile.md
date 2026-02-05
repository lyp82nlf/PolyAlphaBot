# Builder — Profile

Source:
https://docs.polymarket.com/developers/builders/builder-profile

---

## Description

The Builder Profile represents the public-facing identity of a builder
within the Polymarket ecosystem.

It aggregates attribution data, metadata, and performance indicators
associated with a builder_id.

---

## Purpose

- Provide transparency into builder activity.
- Display attribution metrics and rankings.
- Serve as a reference for leaderboards and analytics.

---

## Core Profile Fields

A builder profile typically includes:

- builder_id (string)
  Unique identifier of the builder.

- name (string)
  Display name of the builder.

- description (string)
  Short description of the builder or integration.

- tier (string)
  Current builder tier.

- attributed_volume (string)
  Total trading volume attributed to this builder.

- rank (integer)
  Current leaderboard rank.

---

## Visibility

- Builder profiles are publicly visible.
- Data is aggregated and read-only.
- No private or sensitive information is exposed.

---

## Update Behavior

- Metrics are updated periodically.
- Tier and rank may change as new volume is attributed.

---

## Notes

- Profiles are informational only.
- Builders cannot directly edit performance metrics.
- Accurate attribution is required for meaningful profiles.