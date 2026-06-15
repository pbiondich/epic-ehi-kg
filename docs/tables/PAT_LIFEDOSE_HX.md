# PAT_LIFEDOSE_HX

> This is the patient lifetime dose history information for tracked chemicals in Medication Options. This table displays the information from the Lifetime Dose Tracking activity for a specified patient. Total lifetime dose information is in PAT_LIFEDOSE.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 28  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting’s security utility. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHEMICAL_C_NAME` | VARCHAR | org | The chemical category ID for the chemical that needs to be tracked for lifetime dosing for this patient. |
| 4 | `LIFEDOSE_SOURCE_C_NAME` | VARCHAR |  | The source ID for the chemical that needs to be tracked for lifetime dosing for this patient. Indicates how the chemical was recorded in the patient's record, such as eMAR or accumulative dose activity. |
| 5 | `INPATIENT_DATA_ID` | VARCHAR | shared | The unique ID of the inpatient data store record, populated if LIFEDOSE_SOURCE_C is eMAR, which means we record tracked chemical in eMAR. You could get eMAR information from IP_MAR based on this and INPATIENT_DATA_LN. |
| 6 | `INPATIENT_DATA_LN` | INTEGER |  | If SOURCE_C is MAR, which means we record tracked chemical in eMAR, this is the corresponding line number that this line of chemical traced data related to. You could get eMAR information from IP_MAR based on INPATIENT_DATA_ID and this. |
| 7 | `GIVEN_INST` | DATETIME (Local) |  | The instant that the dose of this line was given to the patient in eMAR. |
| 8 | `SIMP_DOSE_AMT` | NUMERIC |  | The simplified dose amount for the chemical. |
| 9 | `SIMP_DOSE_UNIT_C_NAME` | VARCHAR | org | The simplified dose unit category ID for the chemical that needs to be tracked for lifetime dosing for this patient. |
| 10 | `CALC_DOSE_AMT` | NUMERIC |  | The calculated dose amount for the chemical. |
| 11 | `CALC_DOSE_UNIT_C_NAME` | VARCHAR |  | The calculated dose unit category ID for the chemical that needs to be tracked for lifetime dosing for this patient. |
| 12 | `WEIGHT` | NUMERIC |  | The patient's weight used to calculate dose for the chemical at time of administration. |
| 13 | `HEIGHT` | NUMERIC |  | The patient's height used to calculate dose for the chemical at time of administration. |
| 14 | `USER_ID` | VARCHAR | FK→ | The unique ID of the user who entered chemical data, populated if SOURCE_C is manual. |
| 15 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `LIFEDOSE_STATUS_C_NAME` | VARCHAR |  | The status category ID for this chemical that needs to be tracked for lifetime dosing in this row. It will be "1-ACTIVE" normally, and can be changed to "2-CANCELLED" if the chemical administration that corresponds to this row is cancelled. |
| 17 | `COMMENT_INFO` | VARCHAR |  | A free-text comment entered for lifetime dose tracking, if any exists. |
| 18 | `EMAR_LINE` | INTEGER |  | If a manual entry is created to adjust the dose for an eMAR (electronic Medical Administration Record) line, then the original eMAR line is stored here. |
| 19 | `ORDER_MED_ID` | NUMERIC | FK→ | The unique order ID where this line of administered chemical came from. |
| 20 | `FILED_INST` | DATETIME (Attached) |  | The instant that a manual adjusted entry line is stored. |
| 21 | `REVIEW_STATUS_C_NAME` | VARCHAR |  | The review status category ID for lifetime dose after merging or unmerging a patient record, or moving information from one patient's record to another patient's record. |
| 22 | `REVIEWED_USER_ID` | VARCHAR |  | Specify the user who reviewed the entry for lifetime dose after patient merge, unmerge, or contact move. |
| 23 | `REVIEWED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 24 | `REVIEWED_DTTM` | DATETIME (UTC) |  | The date and time when the lifetime dose review is done after merging or unmerging a patient record, or moving information from one patient's record to another patient's record. |
| 25 | `REVIEW_REASON_C_NAME` | VARCHAR |  | The review reason category ID for why the chemical for this row needs review. |
| 26 | `LIFEDOSE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 27 | `SURGERY_CSN` | NUMERIC |  | The unique ID of the surgical contact which is associated with a procedure log where radiation exposure was documented. Use this column to join to PAT_OR_ADM_LINK.PAT_ENC_CSN_ID and the invasive procedure log ID can be found in the column LOG_ID. |
| 28 | `ENTRY_HAS_INCOMPLETE_DATA_YN` | VARCHAR |  | Indicates whether the associated entry has incomplete dosing information that may need further review. 'Y' indicates there is incomplete dosing information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

