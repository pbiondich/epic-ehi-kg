# HSPC_HIS_SUBM

> This table extracts information about the submissions of Hospice Item Set (HIS) dataset records.

**Primary key:** `DATASET_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DATASET_ID` | NUMERIC | PK shared | The unique identifier for the data set record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `HIS_SUBM_TYPE_C_NAME` | VARCHAR | org | Stores the type of HIS submission in the submission history. |
| 6 | `HIS_SUBM_INST_MRK_DTTM` | DATETIME (Attached) |  | Instant that HIS submission was marked. |
| 7 | `HIS_SUBM_USER_ID` | VARCHAR |  | The unique identifier of the user who submitted the HIS data set. Links to table CLARITY_EMP. |
| 8 | `HIS_SUBM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `HIS_SUBM_FILE_DATE_DTTM` | DATETIME (Local) |  | The instant of the HIS submission. |
| 10 | `HIS_SUBM_CORRCT_NUM` | VARCHAR |  | HIS submission correction number. |
| 11 | `HIS_SUBM_KEY_ITEMS` | VARCHAR |  | HIS submission key items history information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

