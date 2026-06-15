# HH_OASIS_SUBM

> Contains information on the submission of Home Health Outcome and Assessment Information Set (OASIS) data sets.

**Primary key:** `OASIS_SET_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OASIS_SET_ID` | NUMERIC | PK FK→ | Unique identifier for the OASIS data set. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | Unique identifier for this contact for this patient. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 4 | `OASIS_SUBM_TYPE_C_NAME` | VARCHAR | org | OASIS data set submission type. Links to category list ZC_OASIS_SUBM_TYPE. Submission, correction, resubmission, inactivation. |
| 5 | `OASIS_SUBM_INST_MK` | DATETIME (Attached) |  | Instant at which OASIS data set is marked submitted. |
| 6 | `OAS_SUBM_USER_ID` | VARCHAR |  | User ID of user who submitted OASIS data set. Links to table CLARITY_EMP. |
| 7 | `OAS_SUBM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `OAS_SUBM_FILE_INST` | DATETIME (Local) |  | Instant at which OASIS submission was filed. |
| 9 | `OAS_SUBM_CRRCT_NUM` | VARCHAR |  | OASIS submission correction number. |
| 10 | `OASIS_SUBMIT_QUE_C_NAME` | VARCHAR | org | OASIS data set's position in submission queue. Links to category list ZC_OASIS_SUBMIT_Q. |
| 11 | `QUEUE_HISTORY_C_NAME` | VARCHAR |  | OASIS data set submission queue history. Links to category table ZC_OASIS_SUBMIT_Q. |
| 12 | `SUBM_QUEUE_DT_INDX` | VARCHAR |  | OASIS submission queue index item. |
| 13 | `HISTORY_INDEX` | VARCHAR |  | OASIS submission queue history index. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OASIS_SET_ID` | [HH_OASIS_INFO](HH_OASIS_INFO.md) | sole_pk | high |

