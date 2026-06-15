# OR_LOG_PROC_CARE_PROTCL

> This table stores the list of clinical protocols a patient is on for their procedure such as enhanced recovery.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LOG_PROC_PROTCL_C_NAME` | VARCHAR | org | A list of clinical protocols the patient is on for their procedure such as enhanced recovery. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

