# REQ_PAT_ADDL_ADDRESS

> Store the additional address information for a patient address.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier for the requisition record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDL_FIELD_C_NAME` | VARCHAR |  | The type of additional address data (floor, unit, building name, etc.) stored in the related field. |
| 4 | `ADDL_DATA` | VARCHAR |  | The additional address data that applies to the additional address data type entered (floor, unit, building name, etc.). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

