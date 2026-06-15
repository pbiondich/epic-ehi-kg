# ENROLL_INFO_HX

> The ENROLL_INFO_HX contains a history of changes to information pertaining to a patient's enrollment in a research study.

**Overflow family:** [ENROLL_INFO_HX_1](ENROLL_INFO_HX_1.md)  
**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique ID of the patient enrollment record for this row. This column is frequently used to link to the ENROLL_INFO table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_MOD_STATUS_C_NAME` | VARCHAR | org | A history of status category number changes for the enrollment. |
| 4 | `HX_MOD_ALIAS` | VARCHAR |  | A history of changes to patient's alias for the enrollment. |
| 5 | `HX_MOD_START_DT` | DATETIME |  | A history of start date changes for the enrollment. |
| 6 | `HX_MOD_END_DT` | DATETIME |  | A history of end date changes for the enrollment. |
| 7 | `HX_MOD_NOTE_CMT_CSN` | NUMERIC |  | A history of the changes to the comments note record associated with the enrollment. |
| 8 | `HX_MOD_DTTM` | DATETIME (Local) |  | Instant that the enrollment information was modified. |
| 9 | `HX_MOD_USER_ID` | VARCHAR |  | User who modified the enrollment information. |
| 10 | `HX_MOD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `HX_MOD_BRANCH_ID` | VARCHAR |  | This item stores a history of the branches (arms) in a research study to which the patient has been assigned. |
| 12 | `HX_MYCHART_STATUS_C_NAME` | VARCHAR |  | History of the enrollment's MyChart recruitment status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

