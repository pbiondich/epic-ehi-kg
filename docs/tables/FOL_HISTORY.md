# FOL_HISTORY

> Activity history table for this follow-up record.

**Primary key:** `FOL_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FOL_ID` | NUMERIC | PK FK→ | Follow-up record unique identifier |
| 2 | `LINE` | INTEGER | PK | This is the line number. Together with the FOL_ID, this column uniquely defines each row in this table. |
| 3 | `ACT_ACTION_TYPE_C` | INTEGER |  | When the activity is 30-Action, this is the Action Type category ID for the related follow-up record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FOL_ID` | [FOL_INFO](FOL_INFO.md) | sole_pk | high |

