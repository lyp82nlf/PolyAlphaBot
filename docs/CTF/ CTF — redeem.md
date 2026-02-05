# CTF — Redeem

Source:
https://docs.polymarket.com/developers/CTF/redeem

---

## Description

Redeems winning conditional outcome tokens for collateral after a condition
has been resolved.

Once the oracle resolves a condition, only the winning outcome token(s)
can be redeemed for collateral. Losing outcome tokens become worthless.

---

## Purpose

- Settle positions after market resolution.
- Convert winning outcome tokens back into collateral.
- Finalize the lifecycle of a conditional token.

---

## Preconditions

- The condition MUST be resolved by the oracle.
- The caller MUST hold winning outcome tokens.
- Losing outcome tokens cannot be redeemed.

---

## Key Parameters

- collateralToken (address)
  ERC-20 token used as collateral (e.g. USDC).

- conditionId (bytes32)
  Identifier of the resolved condition.

- parentCollectionId (bytes32)
  Collection ID of the parent condition.
  Use 0x0 for top-level conditions.

- indexSets (uint256[])
  Array of index sets representing winning outcome slots.

---

## Index Sets Explained

- Index sets are bitmasks identifying winning outcome slots.
- Only index sets that match the oracle-reported result are redeemable.

Example (binary):
- YES wins → indexSet = 0b01 (1)
- NO wins  → indexSet = 0b10 (2)

---

## Contract Call

Function:
 redeemPositions(
   address collateralToken,
   bytes32 parentCollectionId,
   bytes32 conditionId,
   uint256[] calldata indexSets
 )

---

## Example (Binary Market)

Condition resolved:
 YES wins

User holds:
 - 100 YES tokens
 - 0 NO tokens

Redeeming:
 - YES tokens burned: 100
 - Collateral received: 100 units

---

## Notes

- Redemption is only possible after resolution.
- Gas is required.
- This is the only way to extract value after resolution.