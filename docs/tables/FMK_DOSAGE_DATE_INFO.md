# FMK_DOSAGE_DATE_INFO

> This table holds information related to the dosage start date for FMK.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FMK_DOSAGE_START_DATE` | DATETIME |  | Dosage start date that should be considered to send to FMK. |
| 4 | `FMK_DOSAGE_CHNG_RSN_C_NAME` | VARCHAR | org | Stores the description of the action that caused the dosage to update. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

