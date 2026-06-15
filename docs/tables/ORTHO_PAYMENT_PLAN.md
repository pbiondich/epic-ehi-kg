# ORTHO_PAYMENT_PLAN

> The ORTHO_PAYMENT_PLAN table contains information about orthodontics charging plans.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | VARCHAR | PK shared | The unique identifier for the dental billing plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORTHO_PMT_PLAN_NUM` | INTEGER |  | The orthodontic charging plan number. |
| 4 | `ORTHO_PAT_INS_LIAB` | NUMERIC |  | The patient or insurance liability of the orthodontic charging plan. |
| 5 | `ORTHO_PATIENT_YN` | VARCHAR |  | Indicate whether this charging plan line is for the self-pay portion of this charging plan. |
| 6 | `ORTHO_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 7 | `ORTHO_LIABILITY` | NUMERIC |  | The self-pay or insurance portion for this orthodontic charging plan line. |
| 8 | `ORTHO_DOWN_PAYMENT` | NUMERIC |  | The amount of the initial charge for this charging plan line. |
| 9 | `ORTHO_TERM_LENGTH` | INTEGER |  | The frequency of payments for this orthodontic charging plan line measured in months. |
| 10 | `ORTHO_TOTAL_TERMS` | INTEGER |  | The number of payments included in this orthodontic charging plan line. |
| 11 | `ORTHO_TERMS_LEFT` | INTEGER |  | The number of payments left on this orthodontic charging plan line. |
| 12 | `ORTHO_TERM_PAY` | NUMERIC |  | The amount of the payments for this orthodontic charging plan line. |
| 13 | `ORTHO_LAST_TERM_PAY` | NUMERIC |  | The amount of the final payment for this orthodontic charging plan line. |
| 14 | `ORTHO_START_DATE` | DATETIME |  | The date this charging plan line starts. |
| 15 | `ORTHO_DATE_ESTAB_DT` | DATETIME |  | The date when this orthodontic charging plan line was created. |
| 16 | `ORTHO_ACTIVE_YN` | VARCHAR |  | Indicates whether this charging plan line is active or not. Y indicates that this line is active. N or a null value indicates that this line is not active. |
| 17 | `ORTHO_ENTRY_USER_ID` | VARCHAR |  | The unique ID of the user record who entered the orthodontic charging plan line. This column is frequently used to link to the CLARITY_EMP table. |
| 18 | `ORTHO_ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 19 | `ORTHO_ENTRY_TIME` | DATETIME (Local) |  | The time when orthodontic charging plan line was entered in the system. |
| 20 | `ORTHO_DEL_USER_ID` | VARCHAR |  | The unique ID of the user record who removed the orthodontic charging plan line. This column is frequently used to link to the CLARITY_EMP table. |
| 21 | `ORTHO_DEL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 22 | `ORTHO_DEL_DATE` | DATETIME |  | The date when orthodontic charging plan line was removed. |
| 23 | `ORTHO_DEL_TIME` | DATETIME (Local) |  | The time when orthodontic charging plan was removed. |
| 24 | `ORTHO_CHARGING_DATE` | DATETIME |  | The date when the charge was dropped for this payment plan. |
| 25 | `NUM_VISITS_LEFT` | INTEGER |  | The required number of visits which are left for this payment plan term. |
| 26 | `LST_CHG_DT` | DATETIME |  | The last charge dropping date. In order to meet the minimum number of visits, we need to count the number of visits from the last charge dropping date to the current charge dropping date. |
| 27 | `NUM_OF_VIS_REQ` | INTEGER |  | Number of visits required by payer for the charging plan period. |
| 28 | `ORTHO_INITIAL_CHG_DATE` | DATETIME |  | Date to be used for the initial charge on this current charging plan line. |
| 29 | `ORTHO_INITIAL_CHG_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 30 | `ORTHO_PERIODIC_CHG_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

