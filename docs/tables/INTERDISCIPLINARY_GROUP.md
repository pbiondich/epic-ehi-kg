# INTERDISCIPLINARY_GROUP

> This table contains a list of the interdisciplinary group members who reviewed a patient's plan of care as documented in a Plan of Care (POC) or POC update.

**Primary key:** `POC_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `POC_ID` | NUMERIC | PK | The unique identifier for the plan of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IDG_MEM_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `IDG_MEM_DISCPLN_C_NAME` | VARCHAR | org | This item stores the discipline of the interdisciplinary group member. |
| 5 | `IDG_INST_ADDED_DTTM` | DATETIME (UTC) |  | This item stores the instant when an interdisciplinary group member was added. |
| 6 | `IDG_USER_ADDED_ID` | VARCHAR |  | The unique ID associated with the user who added the interdisciplinary group member. |
| 7 | `IDG_USER_ADDED_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

