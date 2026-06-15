# DD_DIA_CMS_START_NO_HOME

> This table contains the reasons why a patient was not informed of home dialysis options as submitted for CMS ESRD patient registration forms (CMS-2728).

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DD_DIA_CMS_START_NO_HOME_C_NAME` | VARCHAR |  | The dialysis patient not informed of home dialysis reasons category ID for the CMS Form 2728 abstraction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

