# OB_HSB_DATING

> This table contains the associated information about the criteria for determining the estimated date of delivery for this pregnancy.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 20  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID assigned to the episode record (HSB .1). |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `OB_DT_EVENT_C_NAME` | VARCHAR | org | The event or criterion that identifies this line in the dating table. |
| 4 | `OB_DT_DTESYS_DT` | DATETIME |  | The system-calculated date when this event occurred. |
| 5 | `OB_DT_DTEUSR_DT` | DATETIME |  | The date when this event occurred, as entered by the user. |
| 6 | `OB_DT_GA_SYS` | INTEGER |  | The gestational age at which this event is expected to occur, as calculated by the system. This value represents the gestational age in days. |
| 7 | `OB_DT_GA_USR` | INTEGER |  | The gestational age at which this criterion did occur, as specified by the user. This value represents the gestational age in days. |
| 8 | `OB_DT_EDDSYS_DT` | DATETIME |  | The estimated date of delivery based on this criterion, as calculated by the system. |
| 9 | `OB_DT_EDDUSR_DT` | DATETIME |  | The estimated date of delivery based on this criterion, as entered by the user. |
| 10 | `OB_DT_WRKEDD_YN` | VARCHAR |  | If this column is yes, then the current event is the one that is considered the working estimated date of delivery for this pregnancy. |
| 11 | `OB_DT_ENTINS_TM` | DATETIME (Local) |  | The instant this row was entered and saved. |
| 12 | `OB_DT_ENTUSR_ID` | VARCHAR |  | The user who has entered the information for this specific dating event. |
| 13 | `OB_DT_ENTUSR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `OB_DT_CYC_LN` | INTEGER |  | The patient's average menstrual cycle length. |
| 15 | `OB_DT_LUT_LN` | INTEGER |  | The average length of the menstrual cycle's luteal phase. |
| 16 | `OB_DT_AFTOVU` | INTEGER |  | The number of days after ovulation that conception occurred. |
| 17 | `OB_DT_ENT_CMT` | VARCHAR |  | A comment for this event. |
| 18 | `OB_DT_BTHCTL_YN` | VARCHAR |  | If yes, the patient was on birth control at the time of conception. |
| 19 | `OB_DT_DTEPREC_C_NAME` | VARCHAR | org | This item represents the uncertainty of the date in column OB_DT_DTEUSR_DT. Category table ZC_OB_DT_DTEPREC maps the category numbers to their names. |
| 20 | `OB_DT_REASONCHNG_C_NAME` | VARCHAR | org | This item contains the user-supplied reason for changing the working EDD of a pregnant patient. This improves the auditing of pregnancy dating events. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

