# HSP_BDC_REV_CODE

> This table contains the user-entered revenue code overrides for follow-up records (i.e. denials).

**Primary key:** `BDC_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the denial or correspondence record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REVENUE_CODE_ID` | NUMERIC |  | This item is the user overridden revenue code for the denial. |
| 4 | `REVENUE_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

