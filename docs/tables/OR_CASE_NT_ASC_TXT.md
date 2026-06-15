# OR_CASE_NT_ASC_TXT

> This table includes the reason the patient is going to an Inpatient OR instead of an ASC.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RSN_CASE_NOT_ASC` | VARCHAR |  | The reason a case is being done in an Inpatient Operating Room (IP OR) instead of an Ambulatory Surgery Center (ASC). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

