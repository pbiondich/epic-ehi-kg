# ORDER_RAD_STUDY

> This table stores information about actions performed on the study in imaging departments.

**Primary key:** `ORDER_PROC_ID`, `CONTACT_DATE_REAL`  
**Columns:** 17  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the order record associated with this procedure order. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `STUDY_MODE_C_NAME` | VARCHAR |  | The mode category ID for this study (Study Review, Transcription Entry). |
| 4 | `USER_ID` | VARCHAR | FK→ | The user ID of the user performing the study action. |
| 5 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 7 | `STUDY_CHAR_CNT` | INTEGER |  | The character count for the current study. Typically used to track transcriptionist productivity. |
| 8 | `AUDIT_ACT_C_NAME` | VARCHAR |  | The action category ID for the study (sent to transcription, signed, etc.) |
| 9 | `STUDY_TIME` | INTEGER |  | The amount of time (in seconds) the study was open. |
| 10 | `DISCREPANCY_C_NAME` | VARCHAR | org | The discrepancy category ID, populated when another physician has a discrepancy with the previous result for this exam. |
| 11 | `DISCREPANCY_CMNT` | VARCHAR |  | A free text comment associated with a discrepancy. |
| 12 | `DISCREPANCY_READ_YN` | VARCHAR |  | Indicates whether a discrepancy has been acted on for this order. 'Y' indicates the discrepancy has been acted upon. |
| 13 | `STUDY_LINE_CNT` | INTEGER |  | This stores the number of imaging result text lines added with the contact. It is intended to be used in imaging transcription productivity reporting. STUDY_CHAR_CNT and STUDY_WORD_CNT can also be used for character and word counts of result text added in any given contact. All contacts should be reported on, not just the most recent contact. |
| 14 | `STUDY_FINDING_SDE_COUNT` | INTEGER |  | Total number of SmartData elements from study findings documented on the contact. |
| 15 | `IMAGING_STUDY_USER_TYPE_C_NAME` | VARCHAR |  | The imaging study user type category ID for this user for this order's contact from Study Review. |
| 16 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 17 | `POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

