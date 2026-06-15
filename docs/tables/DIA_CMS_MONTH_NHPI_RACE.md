# DIA_CMS_MONTH_NHPI_RACE

> This table contains patients' Native Hawaiian or Other Pacific Islander racial identities as submitted for dialysis regulatory reporting forms.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DLYS_NHPI_RACE_C_NAME` | VARCHAR | org | This item is used in dialysis regulatory reporting. It stores a dialysis patient's Native Hawaiian/Other Pacific Islander racial identities. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

