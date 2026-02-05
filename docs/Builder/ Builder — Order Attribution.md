# Builder — Order Attribution

Source:
https://docs.polymarket.com/developers/builders/order-attribution

---

## Description

Order attribution is the mechanism by which trades are credited to a builder.

When an order is placed through a builder-integrated flow, attribution data
is attached so that resulting trades can be associated with that builder_id.

---

## Purpose

- Attribute trading volume to builders.
- Enable leaderboard rankings and incentive calculations.
- Measure the impact of third-party integrations.

---

## Attribution Mechanism (High Level)

1. Builder generates or includes a builder_id.
2. The builder_id is embedded in the order request metadata.
3. The order is executed via Proxy Wallet / Relayer.
4. Trades resulting from the order are recorded with builder attribution.

---

## Key Requirements

- builder_id must be valid and registered.
- Attribution data must be included at order creation time.
- Attribution cannot be added retroactively.

---

## Attribution Scope

- Attribution applies at the order level.
- All fills resulting from an attributed order are credited to the builder.
- Partial fills are proportionally attributed.

---

## Common Pitfalls

- Missing builder_id → no attribution.
- Incorrect builder_id → attribution lost or misassigned.
- Mixing attributed and non-attributed flows unintentionally.

---

## Notes

- Attribution is immutable once the order is created.
- Builders should validate attribution in testing environments.