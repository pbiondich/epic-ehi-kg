# REQ_PAT_COMM_COMMENTS

> The REQ_PAT_COMM_COMMENTS table contains information about comments related to communication with the patient about the requisition.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the requisition record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMMENTS` | VARCHAR |  | The comments entered by the user when they tried to reach the patient associated with this requisition. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

