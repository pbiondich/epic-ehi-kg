# DOCS_RCVD_SOCIALCARE_EPSD

> External documents for Compass Rose episodes.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 25  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `EPISODE_REFERENCE_ID` | VARCHAR |  | The unique reference ID associated with the Compass Rose episode. |
| 6 | `EPISODE_CSN_ID` | NUMERIC |  | CSN of the source DXR record which contains the compass rose episode data. |
| 7 | `SINGLE_SRC_ORG_ID` | NUMERIC |  | The source organization for the compass rose episode data. |
| 8 | `SINGLE_SRC_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 9 | `EPSD_PRIMARY_PROB_DEDUP_REF_ID` | VARCHAR |  | The de-duplicated primary problem associated with this episode. |
| 10 | `EPSD_PROGRAM_EPSD_DEDUP_REF_ID` | VARCHAR |  | The program episode de-duplicated reference ID associated with this episode. |
| 11 | `EPSD_START_DATE` | DATETIME |  | The date the episode was started. |
| 12 | `EPSD_ENROLLMENT_DATE` | DATETIME |  | The date the patient was enrolled in the program. |
| 13 | `EPSD_CALC_ENROLLMENT_DATE` | DATETIME |  | The date the patient was calculated to be enrolled in the program. |
| 14 | `EPSD_END_DATE` | DATETIME |  | The date the program was ended. |
| 15 | `EPSD_CCM_EPISODE_TYPE_C_NAME` | VARCHAR | org | Indicates whether the Coordinated Care Management episode is for a program or for a service. |
| 16 | `EPSD_TYP_ID_C_NAME` | VARCHAR | org | The episode class for the episode. |
| 17 | `EPSD_CMGMT_PROG_CAT_C_NAME` | VARCHAR |  | The program category value, which defines the type of program supported by a Compass Rose episode type. |
| 18 | `EPSD_STAT_INFO_C_NAME` | VARCHAR |  | The status of the episode. |
| 19 | `EPSD_CMGMT_STATUS_C_NAME` | VARCHAR |  | The status of the care coordination episode. |
| 20 | `EPSD_START_TO_ENROLL_BUS_DAYS` | INTEGER |  | The number of business days between when the episode started and when the patient was enrolled in the program associated with the episode. |
| 21 | `EPSD_ENROLL_TO_END_BUS_DAYS` | INTEGER |  | The number of days between when the patient was enroll in the program associated with the episode and when the episode ended in business days. |
| 22 | `EPSD_START_TO_END_BUS_DAYS` | INTEGER |  | The number of days between when the episode started and ended in business days. |
| 23 | `EPSD_START_TO_CALCENR_BUS_DAYS` | INTEGER |  | The number of days between when the episode started and the calculated enrollment date for the patient in the program in business days. |
| 24 | `EPSD_CALCENR_TO_END_BUS_DAYS` | INTEGER |  | The number of days between when the patient was calculated enrolled in the program and when the episode ended in business days. |
| 25 | `EPSD_PROGRAM_NAME` | VARCHAR |  | The name for the Compass Rose episode program. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

