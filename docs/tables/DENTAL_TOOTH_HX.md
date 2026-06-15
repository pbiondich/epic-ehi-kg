# DENTAL_TOOTH_HX

> This table contains the history of edits for a dental tooth record.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENTAL_PATIENT_CSN` | NUMERIC |  | Stores the patient encounter in which a particular contact of the record was modified if it was available. |
| 4 | `DENTAL_MOD_USER_ID` | VARCHAR |  | Stores the user who modified the tooth record. |
| 5 | `DENTAL_MOD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `DENTAL_MOD_INSTANT_DTTM` | DATETIME (Attached) |  | Stores the date and time when the tooth record was modified. |
| 7 | `DEN_TOO_STAT_HIST_C_NAME` | VARCHAR |  | Keeps track of how status of a tooth changes over time. |
| 8 | `DENT_ACTIVE_HIST_C_NAME` | VARCHAR |  | This column keeps track of whether a tooth was shown in the tooth chart over time. |
| 9 | `DENT_CHRON_INSTANT_DTTM` | DATETIME (Attached) |  | This is the date and time the documentation was made for, such as when documenting past historical data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

