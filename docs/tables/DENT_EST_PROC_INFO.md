# DENT_EST_PROC_INFO

> The DENT_EST_PROC_INFO table contains information about predetermination procedures for a billing plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | VARCHAR | PK shared | The unique identifier for the treatment plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `PROC_DESC` | VARCHAR |  | The name/description of the procedure which is associated with this dental treatment plan. |
| 5 | `PROC_QTY` | INTEGER |  | The quantity of the dental treatment procedure. |
| 6 | `PROC_CHG_AMT` | NUMERIC |  | The charge amount for the dental treatment procedure performed. |
| 7 | `PROC_ENTRY_DATE` | DATETIME |  | The date when the procedure entered into the system. |
| 8 | `PROC_DELETED_YN` | VARCHAR |  | Indicates whether a procedure is deleted for this dental treatment plan. Y indicates that the procedure is deleted. N or a null value indicates that procedure is not deleted. |
| 9 | `PROC_MODIFIER` | VARCHAR |  | The procedure modifier used for the dental treatment procedure. |
| 10 | `PROC_ENTRY_USER_ID` | VARCHAR |  | The unique ID of the user record who entered the procedure. This column is frequently used to link to the CLARITY_EMP table. |
| 11 | `PROC_ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `PROC_ENTRY_TIME` | DATETIME |  | The time when the procedure entered into the system. |
| 13 | `PROC_DEL_USER_ID` | VARCHAR |  | The unique ID of the user record who deleted the procedure. This column is frequently used to link to the CLARITY_EMP table. |
| 14 | `PROC_DEL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `PROC_DEL_DATE` | DATETIME |  | The date when the procedure was deleted from the system. |
| 16 | `PROC_DEL_TIME` | DATETIME |  | The time when the procedure was deleted from the system. |
| 17 | `PROC_TOOTH_NUM_C_NAME` | VARCHAR |  | The number of the tooth on which procedure was performed. |
| 18 | `PROC_SURFACE` | VARCHAR |  | The dental surface where the procedure was performed. |
| 19 | `PROC_ARCH_C_NAME` | VARCHAR |  | The dental surface category number for this procedure. |
| 20 | `PROC_QUADRANT_C_NAME` | VARCHAR |  | The quadrant category number for this dental procedure. |
| 21 | `PROC_AREA` | VARCHAR |  | The dental area where the procedure was performed. |
| 22 | `SUPERNUMRY_YN` | VARCHAR |  | Indicates whether a dental procedure is supernumerary for this dental treatment plan. Y indicates that the procedure is supernumerary. N or a null value indicates that procedure is not supernumerary. |
| 23 | `PROC_FINDING_ID` | NUMERIC |  | Links the dental treatment plan record to any corresponding dental procedure records that were pulled from to create it. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

