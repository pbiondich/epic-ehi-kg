# LOG_CLAVIEN_SCORE

> This table contains Surgical Log (ORL) items related to Clavien Scores for procedural complications.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLAVIEN_SCORE_C_NAME` | VARCHAR | org | This item contains the documented Clavien score that defines complication severity for a procedure on a log. |
| 4 | `CLAVIEN_PROC_ID` | VARCHAR |  | This item contains each procedure on a log requiring a Clavien score that has been documented. |
| 5 | `CLAVIEN_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

