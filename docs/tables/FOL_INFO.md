# FOL_INFO

> PB Insurance Follow-up Workqueue general items table.

**Primary key:** `FOL_ID`  
**Columns:** 2  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FOL_ID` | NUMERIC | PK | This is the follow up record ID. |
| 2 | `TRANSACTION_ID` | NUMERIC | FK→ | Link to the follow-up records corresponding charge record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TRANSACTION_ID` | [CAP_DTL_TX](CAP_DTL_TX.md) | sole_pk | high |

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [BDC_PB_CHGS](BDC_PB_CHGS.md) | `FOL_ID` | high |
| [FOL_HISTORY](FOL_HISTORY.md) | `FOL_ID` | high |

