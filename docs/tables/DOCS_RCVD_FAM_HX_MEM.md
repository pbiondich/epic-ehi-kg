# DOCS_RCVD_FAM_HX_MEM

> This table stores discrete information about family members with a noted medical history. The information stored in this table was received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 23  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `FAMILY_MEMBER_REL` | VARCHAR |  | The patient's relationship to the family member for this row. |
| 6 | `FAMMEMBER_REL_ID_C_NAME` | VARCHAR | org | The category ID of the patient's relationship for the family member for this row. |
| 7 | `FAMILY_MEMBER_NAME` | VARCHAR |  | The name of the family member for this row. |
| 8 | `FAMILY_MEMBER_RFRID` | VARCHAR |  | The unique ID of the relationship of the family member for this row. |
| 9 | `FAMILY_MMB_BIRTHTIM_DTTM` | DATETIME (Attached) |  | The birth date and time of the family member for this row. |
| 10 | `FAMILY_MMB_ISDEC_YN` | VARCHAR |  | The value that determines whether the family member for this row is deceased. |
| 11 | `FAMILY_MMB_DEC_TIME_DTTM` | DATETIME (Attached) |  | The deceased date and time of the family member for this row. |
| 12 | `FAMILY_MMB_SRC_CSN` | NUMERIC |  | The Contact Serial Number of the received document record from which the family member for this row was sourced. |
| 13 | `FAM_MEM_GENDER_C_NAME` | VARCHAR |  | The sex assigned at birth of the family member for this row. |
| 14 | `FAM_MMB_LSTUPD_INST_DTTM` | DATETIME (UTC) |  | Stores the last update instant of the family member's relationship to the patient in UTC. |
| 15 | `FAMILY_MMB_REL_REM_YN` | VARCHAR |  | The value that determines if the family member in this row was marked to be removed by the patient. |
| 16 | `FAM_MMB_UNIQUEID` | VARCHAR |  | The unique identifier for the family relationship in this row that distinguishes this relationship from others made by the same patient. |
| 17 | `FAM_STAT_STATUS_C_NAME` | VARCHAR |  | Stores the status of the family member |
| 18 | `FAM_MMB_FATHER_IDENT` | VARCHAR |  | Holds the Unique ID of the relative who is biological father |
| 19 | `FAM_MMB_MOTHER_IDENT` | VARCHAR |  | Holds the Unique ID of the relative who is biological mother |
| 20 | `FAM_STAT_GENDER_IDENTITY_C_NAME` | VARCHAR | org | Family member gender identity |
| 21 | `FAM_MMB_DOB_DATE` | DATETIME |  | Family member date of birth Used to calculate Age |
| 22 | `FAM_MMB_DOB_END_DATE` | DATETIME |  | Family member date of birth range end. Used for calculating fuzzy age. |
| 23 | `FAM_MMB_DEATH_AGE` | VARCHAR |  | Family Member Death Age |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

