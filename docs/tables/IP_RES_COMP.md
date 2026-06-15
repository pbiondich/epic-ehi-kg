# IP_RES_COMP

> The IP_RES_COMP table contains information about the restraint assessments that must be documented. The information includes details about the order, assessment, and frequent monitoring.

**Primary key:** `INPATIENT_DATA_ID`, `RES_TYPE`, `EPISODE_NUM`, `DOC_TYPE`, `ROW_TYPE_BH`, `ROW_TYPE_MS`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RES_TYPE` | VARCHAR | PK | Displays the restraint type. The restraint can be a behavioral (BH) or nonbehavioral/medical-surgical (MS) restraint. |
| 2 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique ID of the inpatient data store record. |
| 3 | `EPISODE_NUM` | INTEGER | PK | Displays the episode number for the admission. The number assigned to an episode increases with each new episode and does not repeat until a new admission. An episode is the length of a restraint order. A value of '0' represents that there were errors for the corresponding restraint type in the current inpatient data record. |
| 4 | `DOC_TYPE` | VARCHAR | PK | Displays whether the restraint documentation is done once per episode or periodically during a restraint episode. The one-time documentation will have a DOC_TYPE of INFO and the periodic documentation will have a DOC_TYPE of MONITOR. |
| 5 | `COMPLIANT` | VARCHAR |  | Determines whether the compliance measure for the particular episode is compliant by displaying a "Y" or "N". If it cannot be determined a "-" will be displayed. |
| 6 | `COMP_VALS` | VARCHAR |  | Displays the compliant data that was filed for the compliance measures that are only documented once per episode. |
| 7 | `ROW_TYPE_BH` | INTEGER | PK | Displays ID number of the value of compliance measure being reported on within the "Violent Restraint Monitoring Row Type" category list. If the row does not apply to a Violent Restraint, then a value of 999 will be displayed. |
| 8 | `ROW_TYPE_MS` | INTEGER | PK | Displays ID number of the value of compliance measure being reported on within the "Non Violent Restraint Monitoring Row Type" category list. If the row does not apply to a Non Violent Restraint, then a value of 999 will be displayed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

