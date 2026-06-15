# HEMO_DATA_PHASES

> This table contains the phases of an invasive procedure performed in a catheterization lab. It is used to group hemodynamic pressure measurements together by phase.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HEMO_PHASES_KEY` | VARCHAR |  | A unique string to identify the phase. |
| 4 | `HEMO_PHASE_C_NAME` | VARCHAR | org | Stores the phase description that the user chose from the preconfigured options, example: resting. |
| 5 | `USER_ENTERED_PHASE_NAME` | VARCHAR |  | Stores the phase description that a user typed in instead of choosing from the preconfigured options. |
| 6 | `PHASE_START_UTC_DTTM` | DATETIME (UTC) |  | The date and time the phase began (UTC). |
| 7 | `PHASE_END_UTC_DTTM` | DATETIME (UTC) |  | The date and time the phase ended (UTC). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

