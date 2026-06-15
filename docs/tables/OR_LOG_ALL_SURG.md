# OR_LOG_ALL_SURG

> The OR_LOG_ALL_SURG table contains OR management system log surgeons.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 17  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log which refers to the surgeon. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the surgeon in this surgical log. |
| 3 | `SURG_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `ROLE_C_NAME` | VARCHAR | org | The category value which represents the role for the corresponding surgeon in the surgical log. |
| 5 | `SERVICE_C_NAME` | VARCHAR | org | The category value which represents the kind of service the surgical log falls under. |
| 6 | `START_TIME` | DATETIME (Local) |  | The start date and time for the surgeon in the surgical log. |
| 7 | `END_TIME` | DATETIME (Local) |  | The end date and time for the surgeon in the surgical log. |
| 8 | `TOTAL_LENGTH` | INTEGER |  | The total time a surgeon was needed in the surgical log in seconds. |
| 9 | `PANEL` | INTEGER |  | The panel number in the surgical log in which the surgeon was involved. |
| 10 | `RTLS_OFF_YN` | VARCHAR |  | If set to Yes, Real Time Location System (RTLS) tracking has manually been turned off for this provider on this case log. |
| 11 | `TIME_SOURCE_STATUS_C_NAME` | VARCHAR |  | The source (Manual / RTLS) and status category of this row's start and end time. |
| 12 | `START_TIME_CMT` | VARCHAR |  | The start time comment for the surgeon in the surgical log. |
| 13 | `END_TIME_CMT` | VARCHAR |  | The end time comment for the surgeon in the surgical log. |
| 14 | `START_TIME_DOCU_ID` | VARCHAR |  | The unique ID of the EMP user who documented the start time for each surgeon associated with any panel of the surgical log. |
| 15 | `START_TIME_DOCU_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `END_TIME_DOCU_ID` | VARCHAR |  | The unique ID of the EMP user who documented the end time for each surgeon associated with any panel of the surgical log. |
| 17 | `END_TIME_DOCU_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

