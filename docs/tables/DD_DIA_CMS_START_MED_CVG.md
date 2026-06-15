# DD_DIA_CMS_START_MED_CVG

> This table contains patients' current medical coverage eligibility as submitted for CMS ESRD patient registration forms (CMS-2728).

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DIA_CMS_START_MED_CVG_C_NAME` | VARCHAR |  | This item is used in CMS registration form 2728 reporting. It stores a dialysis patient's current medical coverage eligibility. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

