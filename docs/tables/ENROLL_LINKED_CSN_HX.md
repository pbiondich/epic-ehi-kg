# ENROLL_LINKED_CSN_HX

> This table stores history information about encounters linked to or unlinked from research enrollments.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier for the enrollment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_PRL_CSN` | NUMERIC |  | History information of study protocols linked to the encounter's contact serial numbers (CSN). |
| 4 | `HX_LNK_UNIQ_DAY_NUM` | INTEGER |  | History information of the timeline day linked to this encounter. This value corresponds to the value in ENROLL_TIMELINE.UNIQ_DAY_NUM. |
| 5 | `HX_TPL_CSN` | NUMERIC |  | History information of the treatment plan contact serial number (CSN) linked to the encounter. |
| 6 | `HX_TREATMENTDAY_CSN` | NUMERIC |  | History information of the treatment day contact serial number (CSN) linked to the encounter. |
| 7 | `HX_WHO_LINK_ENC_ID` | VARCHAR |  | History information of the user who linked or unlinked an encounter to a study. |
| 8 | `HX_WHO_LINK_ENC_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `HX_WHEN_LINK_ENC_DTTM` | DATETIME (UTC) |  | History information of UTC formatted instant when user links or unlinks an encounter to a study. |
| 10 | `HX_LINKENC_ACTION_C_NAME` | VARCHAR | org | History information of what action the user takes on encounter-study linkage. |
| 11 | `HX_LINKED_ENC_CSN` | NUMERIC | FK→ | History information of contact serial numbers (CSN) of encounters linked to the study. |
| 12 | `HX_TREATMENT_DAY_LINE` | INTEGER |  | History information of the line number of the treatment day in the treatment plan that this encounter is linked to. |
| 13 | `HX_LINK_ENC_SOURCE_C_NAME` | VARCHAR |  | History information about the method used to link or unlink an encounter to or from a study. Blank is an unspecified process (before the data was collected) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |
| `HX_LINKED_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

