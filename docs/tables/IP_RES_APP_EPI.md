# IP_RES_APP_EPI

> The IP_RES_APP_EPI table links restraint episodes with a restraint application.

**Primary key:** `INPATIENT_DATA_ID`, `RES_TYPE`, `APPLICATION_NUM`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RES_TYPE` | VARCHAR | PK | The restraint type can be a behavioral restraint (BH) or nonbehavioral/medical-surgical restraint (MS). |
| 2 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique ID of the inpatient data store record. |
| 3 | `APPLICATION_NUM` | INTEGER | PK | The APPLICATION_NUM refers to the application number for the admission. The application number assigned to an application increases with each new application and does not repeat until a new admission. Each application indicates the period of time from START to DISCONTINUED of all restraints. There can be multiple episodes (orders) within an application. |
| 4 | `LINE` | INTEGER | PK | Line number for each episode number during the restraint application. |
| 5 | `EPISODE_NUM` | INTEGER |  | The EPISODE_NUM refers to the episode number for the admission. The episode number assigned to an episode increases with each new episode and does not repeat until a new admission. An episode is the length of a restraint order. A value of '0' here represents that there were errors for the corresponding restraint type in the current inpatient data record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

