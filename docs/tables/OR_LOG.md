# OR_LOG

> The OR_LOG table contains information about surgical and procedural log (ORL) records.

**Overflow family:** [OR_LOG_2](OR_LOG_2.md)  
**Primary key:** `LOG_ID`  
**Columns:** 67  
**Org-specific columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the procedural log record for this row. |
| 2 | `SURGERY_DATE` | DATETIME |  | The date on which the case was performed. |
| 3 | `CASE_TYPE_C_NAME` | VARCHAR | org | The category value which identifies the type of the surgical log. |
| 4 | `CASE_CLASS_C_NAME` | VARCHAR | org | The classification category ID for the surgical log. |
| 5 | `TRAUMA_CASE_YN` | VARCHAR |  | Yes/no flag which indicates whether this is a trauma case. |
| 6 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient associated with the procedural log record. |
| 7 | `NUM_OF_PANELS` | INTEGER |  | The number of panels in the surgical log. |
| 8 | `REQUEST_PERSON` | VARCHAR |  | The name of the person requesting the surgery |
| 9 | `TOTAL_TIME_NEEDED` | INTEGER |  | The total time needed for the log in minutes |
| 10 | `REFER_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 11 | `DISCHARGE_TO_C_NAME` | VARCHAR | org | The category list which indicates where the patient was discharged to in the surgical log. |
| 12 | `DISPOSITION_TIME` | DATETIME (Local) |  | The time at which the patient was discharged. NOTE: Only the time value of this field is to be used. The date should always be 1/1/1900 for historical reasons. |
| 13 | `EXPIRED_YN` | VARCHAR |  | Yes/no flag which indicates whether the patient died during the surgery. |
| 14 | `EXPIRED_WHERE_C_NAME` | VARCHAR | org | If needed, indicates where the patient expired. |
| 15 | `EXPIRED_TIME` | DATETIME (Local) |  | If needed, records the time at which the patient expired |
| 16 | `X_RAYS_TAKEN_YN` | VARCHAR |  | Yes/no flag which indicates whether X-rays were taken in the surgical log. |
| 17 | `PREOP_XRAYS_YN` | VARCHAR |  | Yes/no flag which indicates whether pre-op X-rays were taken in the surgical log. |
| 18 | `PREOP_VISIT_YN` | VARCHAR |  | Yes/no flag which indicates whether there was a pre-Op Visit for the surgical log. |
| 19 | `LATEX_ALLERGIC_YN` | VARCHAR |  | Yes/no flag which indicates for the surgical log if the patient has a latex allergy. |
| 20 | `EST_BLOOD_LOSS` | NUMERIC |  | The estimated amount of blood lost during the surgery. |
| 21 | `ROOM_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 22 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 23 | `PRIORITY_C_NAME` | VARCHAR |  | The category list which represents the priority of the surgical log |
| 24 | `STATUS_C_NAME` | VARCHAR | org | The category ID for the log status (Posted, Unposted, Voided, etc.) associated with the log record. This column is frequently used to link to ZC_OR_STATUS. |
| 25 | `SERVICE_C_NAME` | VARCHAR | org | The service category ID for the surgical log. |
| 26 | `SCHED_START_TIME` | DATETIME (Local) |  | The date and time at which the surgery in the surgical log was performed. |
| 27 | `VOID_REASON_C_NAME` | VARCHAR | org | A category list which indicates the reason the log was voided. It is entered by the user that voided that log. |
| 28 | `CHECKIN_INSTANT` | DATETIME (Local) |  | The date and time at which the log was checked-in. |
| 29 | `PATIENT_ESCORT` | VARCHAR |  | The person escorting the patient for the surgery. This is a free text value. |
| 30 | `CASE_REQUEST_ID` | VARCHAR |  | The unique ID of the surgical case attached to this log. |
| 31 | `RECORD_CREATE_DATE` | DATETIME |  | The creation date of this surgical log. |
| 32 | `RESEARCH_IND_C_NAME` | VARCHAR | org | The category value which represents the candidacy of the surgical log for research. |
| 33 | `PACU1_LOC_C_NAME` | VARCHAR | org | The category value which represents the patient's location in the PACU. |
| 34 | `REASON_OVER_C_NAME` | VARCHAR | org | The category value which represents the reason for overnight stay. |
| 35 | `IS_CONFIDENTIAL_YN` | VARCHAR |  | Yes/No flag which indicates whether the log is confidential or not (yes indicates confidential). |
| 36 | `ADDENDA_COUNT` | INTEGER |  | The number of addenda on posted logs. This will return the number of addenda on the log if the log status is posted, otherwise, returns null. |
| 37 | `PATIENT_ID_VERB_YN` | VARCHAR |  | Yes/No value indicating whether or not the patient was identified verbally. |
| 38 | `PAT_HAS_ID_BAND_YN` | VARCHAR |  | Yes/No value indicating whether or not the patient has an ID band. |
| 39 | `PAT_BLOOD_BAND_YN` | VARCHAR |  | Yes/No value indicating whether or not the patient has a blood band. |
| 40 | `BLOOD_BAND_NUMBER` | VARCHAR |  | The number of the patient's blood band. |
| 41 | `INTRAOP_DISCH_TO_C_NAME` | VARCHAR | org | The category value which indicates to where the patient was discharged. |
| 42 | `SURGEON_COST` | NUMERIC |  | The cost associated with the surgeons. The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| 43 | `ANES_STAFF_COST` | NUMERIC |  | The cost associated with the anesthesia staff. The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| 44 | `OR_COST` | NUMERIC |  | The cost associated with the operating room. The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| 45 | `SURG_STAFF_COST` | NUMERIC |  | The cost associated with the surgical staff. The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| 46 | `SURG_EQUIP_COST` | NUMERIC |  | The cost associated with the surgical equipment. The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| 47 | `ANES_EQUIP_COST` | NUMERIC |  | The cost associated with the anesthesia equipment. The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| 48 | `INSTR_COST` | NUMERIC |  | The cost associated with the surgical instruments. The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| 49 | `PROC_COST` | NUMERIC |  | The cost associated with the procedures. The item from which this column extracts is no longer populated in released workflows, but may include historical data. |
| 50 | `VOID_COMMENTS` | VARCHAR |  | The free text comments entered when the log was voided. |
| 51 | `LOG_ACCEPTED_YN` | VARCHAR |  | Yes/No flag indicating whether or not the log was accepted in Log Entry. |
| 52 | `OR_TIME_EVTS_ENT_C_NAME` | VARCHAR |  | Indicates the timing events status of the case. This is used to see if the case is not started, in progress or done. |
| 53 | `PROC_NOT_PERF_C_NAME` | VARCHAR | org | The category number for the reason why the procedure was not performed. |
| 54 | `PROC_NOT_PERF_COM` | VARCHAR |  | Stores the comments, if the procedure not performed. |
| 55 | `LOG_TYPE_C_NAME` | VARCHAR |  | The type of log category number for the log. |
| 56 | `CASE_ID` | VARCHAR | shared | This column stores the case ID (ORC) for this log. |
| 57 | `BLOOD_LOSS_UNIT_C_NAME` | VARCHAR | org | Unit of measure of blood loss. |
| 58 | `SCHED_INSTR_EDIT_YN` | VARCHAR |  | Stores whether the scheduling instructions were edited. |
| 59 | `PAT_INSTR_EDITED_YN` | VARCHAR |  | Stores whether the patient instructions were edited. |
| 60 | `NURSE_NOTES_EDIT_YN` | VARCHAR |  | Stores whether the nursing notes have been edited. |
| 61 | `POSITION_NOTES_E_YN` | VARCHAR |  | Stores whether the positioning notes have been edited. |
| 62 | `EMERG_STATUS_YN` | VARCHAR |  | Indicates whether there is an emergency status for this log. If the log does have an emergency status, this column will display Y. The column will display N if there is not an emergency status and null if the status was not set. |
| 63 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status category number for this log. |
| 64 | `FORM_ID_COUNTER` | INTEGER |  | Annotated images form ID counter. |
| 65 | `CHRGS_AT_ADDEND_YN` | VARCHAR |  | This item is populated as Yes or No when an addendum is filed, or when log charges are calculated, to indicate whether there are charges to be sent. This item will be set to 1-Yes if there are any new charges, charges to be updated, or charges to be cancelled, or if there are any charge errors or warnings. Otherwise, this item will be set to 2-No. If this item is blank, the log charges will be calculated on the fly by the Log Charges Work List to evaluate whether to include the log in the report. |
| 66 | `PRIMARY_PHYS_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 67 | `PRIMARY_PERFORMING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

