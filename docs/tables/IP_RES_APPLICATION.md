# IP_RES_APPLICATION

> The IP_RES_APPLICATION table contains information about the restraint application, which is the period of time from START to DISCONTINUED. There can be multiple episodes (length of an order) within an application. The table gives the start/end date of the application and the number of episodes within the application.

**Primary key:** `INPATIENT_DATA_ID`, `RES_TYPE`, `APPLICATION_NUM`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RES_TYPE` | VARCHAR | PK | The restraint type can be a behavioral restraint (BH) or nonbehavioral/medical-surgical restraint (MS). |
| 2 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique ID of the inpatient data store record. |
| 3 | `APPLICATION_NUM` | INTEGER | PK | The APPLICATION_NUM refers to the application number for the admission. The application number assigned to an application increases with each new application and does not repeat until a new admission. Each application indicates the period of time from START to DISCONTINUED of all restraints. There can be multiple episodes (length of an order) within an application. |
| 4 | `APP_START_DT` | DATETIME (Local) |  | The application start date refers to the date when the initial restraint had a status of START. There can be multiple episodes (length of an order) within an application, but the application start date is the date of the first episode in a series of episodes back to back. |
| 5 | `APP_END_DT` | DATETIME (Local) |  | The application end date refers to the date when the restraint had a status of DISCONTINUED. There can be multiple episodes (length of an order) within an application, but the application end date is the date of the last episode that is being discontinued. |
| 6 | `EPISODE_MAX_NUM` | INTEGER |  | The number of episodes within the restraint application. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

