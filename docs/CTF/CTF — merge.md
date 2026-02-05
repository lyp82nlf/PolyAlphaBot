# CTF — Merge

Source:
https://docs.polymarket.com/developers/CTF/merge

---

## Description

Merges conditional outcome tokens back into collateral tokens.

This operation is the inverse of split. It burns outcome tokens and releases
the underlying collateral back to the user.

---

## Purpose

- Combine outcome tokens into collateral.
- Exit positions before condition resolution.
- Rebalance or unwind exposure.

---

## Key Parameters

- collateralToken (address)
  ERC-20 token used as collateral (e.g. USDC).

- conditionId (bytes32)
  Identifier of the condition.

- parentCollectionId (bytes32)
  Collection ID of the parent condition.
  Use 0x0 for top-level conditions.

- partition (uint256[])
  Array of outcome slot bitmasks being merged.

- amount (uint256)
  Amount of outcome tokens to merge.

---

## Partition Rules

- Partition must match the partition used in split.
- Outcome token balances must be sufficient for all partition entries.
- All merged tokens are burned.

---

## Contract Call

Function:
 mergePositions(
   address collateralToken,
   bytes32 parentCollectionId,
   bytes32 conditionId,
   uint256[] calldata partition,
   uint256 amount
 )

---

## Example (Binary Market)

Partition:
 [1, 2]

User holds:
 - 50 YES tokens
 - 50 NO tokens

Merging 50 units results in:
 - YES tokens burned: 50
 - NO tokens burned: 50
 - Collateral returned: 50 units

---

## Notes

- Requires holding a complete set of outcome tokens.
- Gas is required.
- Merge is only possible before condition resolution.