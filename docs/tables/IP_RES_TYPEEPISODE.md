# IP_RES_TYPEEPISODE

> The IP_RES_TYPEEPISODE table contains information about the restraint type episodes within a restraint episode. A restraint type episode is defined as the period during which a patient has a single type of restraint applied. The information includes start/end dates, length, and starting department.

**Primary key:** `INPATIENT_DATA_ID`, `RES_TYPE`, `EPISODE_NUM`, `RES_ROW_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RES_TYPE` | VARCHAR | PK | The restraint type can be a behavioral restraint (BH) or nonbehavioral/medical-surgical restraint (MS). |
| 2 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique ID of the inpatient data store record. |
| 3 | `EPISODE_NUM` | INTEGER | PK | The EPISODE_NUM refers to the episode number for the admission. The episode number assigned to an episode increases with each new episode and does not repeat until a new admission. An episode is the length of a restraint order. A value of '0' here represents that there were errors for the corresponding restraint type in the current inpatient data record. |
| 4 | `RES_ROW_ID` | VARCHAR | PK | The unique ID of the flowsheet row record for the type of restraint used. |
| 5 | `RES_ROW_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |
| 6 | `TYPE_START_DT` | DATETIME (Local) |  | The type episode start date refers to the instant for which the flowsheet row for that restraint type had a START documented. |
| 7 | `TYPE_END_DT` | DATETIME (Local) |  | The type episode end date refers to the instant for which the flowsheet row for that restraint type had a DISCONTINUED documented. |
| 8 | `TYPE_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 9 | `TYPE_LENGTH` | FLOAT |  | The length of time in hours that the restraint documentation indicates that the restraint type has been on for. |
| 10 | `LINE` | INTEGER | PK | This column contains a number to uniquely identify different restraint type episodes that have the same episode and restraint row ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

