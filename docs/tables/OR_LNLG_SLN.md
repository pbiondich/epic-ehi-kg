# OR_LNLG_SLN

> This table contains information on sentinel lymph node readings.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SENTINEL_LYMPH_NODE` | VARCHAR |  | Which sentinel lymph node is being documented on |
| 4 | `SLN_LOCATION` | VARCHAR |  | Where the sentinel lymph node is on the patient |
| 5 | `SLN_IN_VIVO_READING` | NUMERIC |  | Reading of the sentinel lymph node bed in vivo |
| 6 | `SLN_EX_VIVO_READING` | NUMERIC |  | Reading of the sentinel lymph node bed ex vivo |
| 7 | `SLN_DYE_PRESENT_C_NAME` | VARCHAR | org | Whether dye is present at the sentinel lymph node bed |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

