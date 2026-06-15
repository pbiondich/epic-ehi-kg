# THRESHOLD_VALUES

> Patient-specific reference range values and related information.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the patient threshold record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `HIGH_VALUE` | VARCHAR |  | High value for the reference range |
| 4 | `LOW_VALUE` | VARCHAR |  | Low value for the reference range |
| 5 | `FROM_TM` | DATETIME (Local) |  | Beginning instant for the reference range for when it should be used |
| 6 | `TILL_TM` | DATETIME (Local) |  | Ending instant for when the reference range should be used |
| 7 | `WHO_CHANGED_ID` | VARCHAR |  | The unique ID representing the employee who entered the data corresponding to this line. |
| 8 | `WHO_CHANGED_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `WHEN_TM` | DATETIME (Local) |  | Instant when the data in this line was changed. |
| 10 | `COMMENTS` | VARCHAR |  | Comments about the reference range represented by the current line. |
| 11 | `FROM_UTC_DTTM` | DATETIME (UTC) |  | Beginning instant (UTC, used for new values) for when this reference range should be used. |
| 12 | `TILL_UTC_DTTM` | DATETIME (UTC) |  | Ending instant (UTC, used for new values) for when this reference range should be used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

