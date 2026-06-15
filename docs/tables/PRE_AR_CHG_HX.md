# PRE_AR_CHG_HX

> This table contains one row for each activity performed on a temporary accounts receivable (TAR) record of type charge. This table contains basic information about the activity (activity code, user, date, and comment). Note: TAR records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `CHARGE_HX_LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique ID of the temporary transaction record. |
| 2 | `CHARGE_HX_LINE` | INTEGER | PK | The line number for the history information associated with this record. This does not correspond to the CHARGE_LINE columns of other PRE_AR_CHG tables. |
| 3 | `ACTIVITY_C_NAME` | VARCHAR |  | The activity performed category ID for the temporary transaction. |
| 4 | `ACTIVITY_DATE` | DATETIME |  | The date when the activity is performed. |
| 5 | `ACTIVITY_EXIT_DT` | DATETIME |  | The date when the "resolve" activity is performed. |
| 6 | `ACTIVITY_TIMESTAMP` | NUMERIC |  | The time when the activity was performed in seconds from 12/31/1840. |
| 7 | `USER_ID` | VARCHAR | FK→ | The unique ID of the user who performed the activity. This column is frequently used to link to the CLARITY_EMP table. |
| 8 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `USER_COMMENT` | VARCHAR |  | The comments that the user added when performing the activity. |
| 10 | `EXIT_TIMESTAMP` | NUMERIC |  | The time when the resolving activity was performed in seconds from 12/31/1840. |
| 11 | `EXIT_USER_ID` | VARCHAR |  | The unique ID of the user who performed the resolving activity. This column is frequently used to link to the CLARITY_EMP table. |
| 12 | `EXIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `EXIT_ACTIVITY_C_NAME` | VARCHAR |  | The category number of the resolving activity. |
| 14 | `DEFER_UNTIL_DTTM` | DATETIME (UTC) |  | Records the date & time (including time zone in UTC format) that a charge session was deferred until. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

