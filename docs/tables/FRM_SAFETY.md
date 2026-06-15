# FRM_SAFETY

> This tables stores the overall safety information for screening forms. This includes the proceed or do not proceed decision, accompanying comments, and the editing users and times.

**Primary key:** `SCREENING_FORM_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCREENING_FORM_ID` | NUMERIC | PK | The unique identifier for the screening form record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FRM_PROCEED_DECISION_C_NAME` | VARCHAR |  | The screening form proceed with exam? category ID for the screening form. |
| 4 | `FRM_PROCEED_CMT` | VARCHAR |  | The user-entered comment of the screening form, indicating why they will or will not proceed with the exam. |
| 5 | `PROCEED_AUD_USER_ID` | VARCHAR |  | The unique ID of the user who edited the proceed flag for the exam. |
| 6 | `PROCEED_AUD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `PROCEED_AUD_DTTM` | DATETIME (UTC) |  | The instants when the proceed flag or comment was edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

