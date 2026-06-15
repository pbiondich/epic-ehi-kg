# DD_DIA_CMS_START_COMORBID

> This table contains patients' comorbid conditions as submitted for CMS ESRD patient registration forms (CMS-2728).

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DIA_CMS_START_COMORBID_C_NAME` | VARCHAR | org | This item is used in CMS registration form 2728 reporting. It stores a dialysis patient's comorbid conditions. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

