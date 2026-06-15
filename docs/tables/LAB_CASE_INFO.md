# LAB_CASE_INFO

> Lab Anatomic Pathology case information.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CASE_TYPE_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 4 | `CASE_NUM` | VARCHAR |  | Case number with type and compiled number generation |
| 5 | `AP_CASE_STATUS_C_NAME` | VARCHAR | org | The status category number for the case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

