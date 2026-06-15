# OR_CASE_BLOOD_PROD

> The OR_CASE_BLOOD_PROD table contains OR management system case blood products.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the blood product information for the case. |
| 3 | `BLOOD_PRODUCT_C_NAME` | VARCHAR | org | The category value which indicates the type of blood product requested for the case. |
| 4 | `BLOOD_ESTIMATED` | NUMERIC |  | The total number of units of the blood product requested for the case. |
| 5 | `BLOOD_MSR_UNIT_C_NAME` | VARCHAR | org | Unit of measurement of the blood product requested for the case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

