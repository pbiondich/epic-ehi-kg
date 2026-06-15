# OR_LNLG_ARR_THERAP

> This table contains the Arrival Therapies information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 4  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `ARR_THER_LOC_C_NAME` | VARCHAR | org | The location at which the arrival therapy was performed. |
| 3 | `ARR_THER_LAT_C_NAME` | VARCHAR | org | The laterality of the location. |
| 4 | `ARR_THER_ITEM_C_NAME` | VARCHAR | org | The category ID as to why arrival therapies were used. Arrival therapies are typically medications the patient is on when they arrive to the unit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

