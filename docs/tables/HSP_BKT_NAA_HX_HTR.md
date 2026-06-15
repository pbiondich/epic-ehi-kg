# HSP_BKT_NAA_HX_HTR

> The HSP_BKT_NAA_TX_HTR table contains the not allowed adjustment transactions posted at each line of the table HSP_BKT_NAA_ADJ_HX.

**Primary key:** `BUCKET_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | This column stores the unique identifier for the bucket record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `NAA_ADJ_HX_HTR_ID` | NUMERIC |  | The permanent transaction in the adjustment table of the contractual adjustment history table. |
| 5 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | Hospital account associated with the liability bucket |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

