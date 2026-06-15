# OR_CASE_INSTR_PICKED

> Contains information about instruments picked for the case.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INSTR_TYPE_PICKED_C_NAME` | VARCHAR | org | List of instrument types picked for the case |
| 4 | `REASON_INSTR_NOT_PICK_C_NAME` | VARCHAR | org | Reason instrument wasn't picked for the case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

