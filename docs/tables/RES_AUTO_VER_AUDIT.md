# RES_AUTO_VER_AUDIT

> This table contains auto verification audit trail information for result (OVR) records for lab.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `AUTO_VER_FAIL_RSN` | VARCHAR |  | The reason why auto verification could not be performed if auto verification failed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

