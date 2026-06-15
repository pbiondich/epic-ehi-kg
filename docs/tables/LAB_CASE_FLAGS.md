# LAB_CASE_FLAGS

> This table contains any flags attached directly to a case record.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CASE_FLAGS_C_NAME` | VARCHAR | org | Stores any flags that are put on the case. |
| 4 | `CASE_FLAGS_CMT` | VARCHAR |  | A free text comment associated with each case flag. |
| 5 | `AP_CASE_FLAG_GRP_C_NAME` | VARCHAR | org | The flag group category ID for the case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

