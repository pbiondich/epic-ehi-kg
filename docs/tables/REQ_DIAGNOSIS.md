# REQ_DIAGNOSIS

> This table contains the associated diagnoses on requisitions.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier for the requisition record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASSOCIATED_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

