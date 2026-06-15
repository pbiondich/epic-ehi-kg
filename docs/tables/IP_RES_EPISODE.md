# IP_RES_EPISODE

> The IP_RES_EPISODE table contains information about the restraint episode. An episode is defined as the length of an order. The information includes episode start/end dates, application start/end dates, episode length, clinical justification documentation, and less restrictive alternatives documentation.

**Primary key:** `INPATIENT_DATA_ID`, `RES_TYPE`, `EPISODE_NUM`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RES_TYPE` | VARCHAR | PK | The restraint type can be a behavioral restraint (BH) or nonbehavioral/medical-surgical restraint (MS). |
| 2 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique ID of the inpatient data store record. |
| 3 | `EPISODE_NUM` | INTEGER | PK | Refers to the episode number for the admission. The number assigned to an episode increases with each new episode and does not repeat until a new admission. An episode is the length of a restraint order. A value of '0' here represents that there were errors for the corresponding restraint type in the current inpatient data record. |
| 4 | `APPLICATION_NUM` | INTEGER |  | Displays the application number for the admission. The number assigned to an application increases with each new application and does not repeat until a new admission. Each application indicates the period of time from START to DISCONTINUED of all restraints. There can be multiple episodes (orders) within an application. |
| 5 | `EPI_START_DT` | DATETIME (Local) |  | The episode start date refers to the date when the flowsheet rows Order Obtained (for behavioral restraints) or Order Upon Application (for nonbehavioral restraints) were documented on in conjunction with the START status of a restraint type row(s). |
| 6 | `EPI_END_DT` | DATETIME (Local) |  | The episode end date refers to the date a new order was obtained (thereby ending the previous episode) or the date that all restraints were DISCONTINUED for the episode. |
| 7 | `EPI_LENGTH` | FLOAT |  | The length of time in hours that the restraint documentation indicates that the restraints have been "on" for. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

