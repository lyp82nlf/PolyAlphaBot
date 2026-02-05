# CTF — Split

Source:
https://docs.polymarket.com/developers/CTF/split

---

## Description

Splits collateral tokens into conditional outcome tokens for a given condition.

This operation converts collateral (e.g. USDC) into ERC-1155 conditional tokens,
one for each outcome slot of the condition.

---

## Purpose

- Lock collateral into the ConditionalTokens contract.
- Mint outcome tokens representing each possible outcome.
- Enable trading of outcome tokens on secondary markets.

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
  Array of outcome slot bitmasks.
  Each element represents a set of outcome slots.

- amount (uint256)
  Amount of collateral to split.

---

## Partition Explained

- Each partition entry is a bitmask.
- Each bit corresponds to an outcome slot.
- For a binary market:
  - YES = 0b01
  - NO  = 0b10

Partitions must:
- Be disjoint (no overlapping bits)
- Cover all desired outcome slots

---

## Contract Call

Function:
 splitPosition(
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

Meaning:
 - Token #1 → outcome slot 0 (YES)
 - Token #2 → outcome slot 1 (NO)

Splitting 100 collateral units mints:
 - 100 YES tokens
 - 100 NO tokens

---

## Notes

- Requires approval of collateral tokens before calling split.
- Gas is required.
- Incorrect partitions will cause the transaction to revert.