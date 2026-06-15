# RES_AP_SYN_REPORTS

> The loaded synoptic reports on a result.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LOADED_SYN_REP_ID` | VARCHAR |  | A list of all the Synoptic Report Forms currently filled out for this result. |
| 4 | `LOADED_SYN_REP_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

