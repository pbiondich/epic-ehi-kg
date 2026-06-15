# CLM_TX_HX_MODIFIERS

> This table stores the history of a service line's procedure modifiers for a given claim.

**Primary key:** `CLAIM_ID`, `LINE`, `PIECE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PIECE` | INTEGER | PK | The piece in the delimited group that the procedure modifier came from. |
| 4 | `MODIFIER_ID` | VARCHAR | FK→ | A procedure modifier that was on one of the service lines of the claim. |
| 5 | `MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `MODIFIER_ID` | [CLARITY_MOD](CLARITY_MOD.md) | sole_pk | high |

