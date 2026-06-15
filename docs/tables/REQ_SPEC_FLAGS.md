# REQ_SPEC_FLAGS

> The REQ_SPEC_FLAGS table contains information about the specimen flags associated with a requisition.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the requisition record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPEC_FLAGS_C_NAME` | VARCHAR | org | The specimen flags category ID for the requistion. |
| 4 | `COMMENTS` | VARCHAR | discont. | The specimen flag comments entered as legacy data. This is legacy data that is no longer populated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

