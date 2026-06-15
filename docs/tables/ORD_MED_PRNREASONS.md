# ORD_MED_PRNREASONS

> This table is to show PRN reasons for all PRN medication orders. If you want to get more information about a medication order, you could link this table to ORDER_MED or ORDER_MEDINFO.

**Primary key:** `ORDER_MED_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the medication order (prescription) record. NOTE: This is an internal unique identifier for order records in this table and cannot be used to link to CLARITY_MEDICATION. |
| 2 | `LINE` | INTEGER | PK | The line number for each PRN reason. |
| 3 | `MED_PRN_REASON_C_NAME` | VARCHAR | org | The PRN reason. |
| 4 | `ORDERING_DATE` | DATETIME |  | The date the order was placed in calendar format. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

