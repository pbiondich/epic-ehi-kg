# AP_CLAIM_MISC_BOX

> The AP_CLAIM_MISC_BOX table contains the miscellaneous box information on an accounts payable claim.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier of the accounts payable claim record. |
| 2 | `LINE` | INTEGER | PK | This column stores the line position in the claim's misc box related items for the current row. |
| 3 | `MISC_BOX_IDENTITY` | VARCHAR |  | The ID of the miscellaneous box entry. |
| 4 | `MISC_BOX_ENTRY` | VARCHAR |  | The miscellaneous entry for the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

