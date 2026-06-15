# FIN_ASST_TRKR_RESTR_AC_CL

> This table contains account class restrictions placed on a financial assistance tracker record to limit the scope of its approval.

**Primary key:** `FIN_ASST_TRACKER_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_TRACKER_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the financial assistance program tracker record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RESTR_ADT_PAT_CLASS_C_NAME` | VARCHAR | org | The account class category ID the financial assistance tracker's approval is restricted to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_TRACKER_ID` | [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | name_stem | high |

