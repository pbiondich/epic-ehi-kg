# MDL_MD_PRBLM_LIST

> The MDL_MD_PRBLM_LIST table enables you to report on Medication Problem List information.

**Primary key:** `MED_PRBLM_LIST_ID`  
**Columns:** 16  
**Joined by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_PRBLM_LIST_ID` | NUMERIC | PK | The unique identifier (.1 item) for the med problem list record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Status of record: 1-inactive, 2-deleted, 4-hidden, 5-inactive and hidden, or 6-deleted and hidden. |
| 3 | `PATIENT_ID` | VARCHAR |  | The Patient ID (EPT) with which this medication problem list (MDL) record is associated. |
| 4 | `CRRNT_LONG_TERM_YN` | VARCHAR |  | The current long-term status of this medication problem list (MDL) record. |
| 5 | `MEDICATION_NOTE_ID` | VARCHAR |  | ID of the note (HNO). This note applies to all patient medications that share the same simple generic medication name. |
| 6 | `SOURCE_PAT_CID` | NUMERIC |  | Source patient CID during patient merge in IntraConnect environments |
| 7 | `MED_ADHER_SCORE` | INTEGER |  | This item stores the most recently calculated medication adherence score for this simple generic. The adherence score is not updated in real time. If you need to ensure a current score for reporting on a population of patients and certain simple generics, you can use a registry with metric HFP 82099-Medication Adherence Score Data. |
| 8 | `MED_ADHER_CONF_C_NAME` | VARCHAR |  | Our confidence that the dispense data used to calculate the medication adherence score is a comprehensive list of dispenses. |
| 9 | `MED_ADHER_ACC_DTTM` | DATETIME (UTC) |  | This item stores the instant that the current score is considered accurate. This is equivalent to the end of the period that we run medication adherence calculation. |
| 10 | `MED_ADHER_DAYSOWNED` | INTEGER |  | This item stores the number of days a patient is supposed to take medications related to this simple generic. This item is accurate to the current medication adherence score. |
| 11 | `MED_ADHER_COVERED` | INTEGER |  | This item stores the number of days that are covered by a patient's supply. Equivalently, it means the patient is being adherent on these days. This item is accurate with the current adherence score. |
| 12 | `MED_ADHER_HIDDEN_C_NAME` | VARCHAR |  | This item stores the reason that the score is hidden. |
| 13 | `MED_ADHER_INST_DTTM` | DATETIME (UTC) |  | This item stores the calculation instant of the current adherence score. |
| 14 | `MED_ADHER_STRT_DATE` | DATETIME |  | This item sets the start date of the Medication adherence score measurement period |
| 15 | `MED_ADHER_ORD_INST_DTTM` | DATETIME (UTC) |  | This item stores the earliest order instant used when calculating the adherence score. |
| 16 | `MED_ADHER_REMAINING` | INTEGER |  | This item stores the estiamted number of days the patient still has on hand. This item is accuate with the current adherence score. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (9)

| From | Column | Confidence |
|------|--------|------------|
| [EXTERNAL_TREATMENT](EXTERNAL_TREATMENT.md) | `MED_PRBLM_LIST_ID` | high |
| [MDL_HISTORY](MDL_HISTORY.md) | `MED_PRBLM_LIST_ID` | high |
| [MDL_RLNOTE_RW_INFO](MDL_RLNOTE_RW_INFO.md) | `MED_PRBLM_LIST_ID` | high |
| [RXFILL](RXFILL.md) | `MED_PRBLM_LIST_ID` | high |
| [RXFILL_DIAGNOSES](RXFILL_DIAGNOSES.md) | `MED_PRBLM_LIST_ID` | high |
| [RXFILL_NOTE](RXFILL_NOTE.md) | `MED_PRBLM_LIST_ID` | high |
| [TREATMENT_PLAN](TREATMENT_PLAN.md) | `MED_PRBLM_LIST_ID` | high |
| [TREATMENT_PLAN_AUDIT](TREATMENT_PLAN_AUDIT.md) | `MED_PRBLM_LIST_ID` | high |
| [TREATMENT_PLAN_TYPE](TREATMENT_PLAN_TYPE.md) | `MED_PRBLM_LIST_ID` | high |

