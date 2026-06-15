# HH_HEIGHT_WEIGHT_HX

> This table contains audit information for patient height and weight recorded during intake.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_WEIGHT` | NUMERIC |  | Auditing history of the patient's weight recorded during home care intake. |
| 4 | `PAT_HEIGHT` | VARCHAR |  | Auditing history of the patient's height recorded during home care intake. |
| 5 | `EDIT_USER_ID` | VARCHAR |  | Auditing history of the user who edited the patient's weight or height during home care intake. |
| 6 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | Auditing history of the instant of edit to a patient's weight or height during home care intake. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

