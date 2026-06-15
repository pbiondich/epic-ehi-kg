# DD_DIA_CMS_START_NO_TXP

> This table contains patients' reasons for not pursuing transplant options as submitted for CMS ESRD patient registration forms (CMS-2728).

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DIA_CMS_START_NO_TXP_C_NAME` | VARCHAR |  | This item is used in CMS registration form 2728 reporting. It stores all the reasons why transplant is not an option for a dialysis patient at this time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

