# MC_PRICER_MCE_EDITS

> MCE edits.

**Primary key:** `PRICER_MSG_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the pricer message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MCE_EDIT_C_NAME` | NUMERIC |  | MCE edits returned from MCE output. |
| 4 | `MCE_EDIT_SCOPE_C_NAME` | NUMERIC |  | Whether the MCE edit applies to a diagnosis code, an ICD-10 procedure code, or another piece of claim data |
| 5 | `MCE_EDIT_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `MCE_EDIT_ICD_PROC_ID` | VARCHAR |  | The ICD-10 procedure code that the MCE edit applies to |
| 7 | `MCE_EDIT_ICD_PROC_ID_ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |
| 8 | `MCE_EDIT_NAME` | VARCHAR |  | The MCE edit's name in the MCE source code |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

