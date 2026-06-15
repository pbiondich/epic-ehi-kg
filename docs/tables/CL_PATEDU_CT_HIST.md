# CL_PATEDU_CT_HIST

> Enterprise reporting table for contact specific education history items in Patient Education (PED) records.

**Primary key:** `PED_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The Unique ID for the Patient Education Record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The Line Count for contact specific history detail. |
| 4 | `CONTACT_DATE` | DATETIME |  | Date of contact for contact specific history detail. |
| 5 | `CONTACT_HX_KEY` | VARCHAR |  | The education key for the contact-specific history record. The education key is a string in the form of Title^Topic^Point. |
| 6 | `CONTCT_HX_TOPIC_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 7 | `CONTCT_HX_POINT_ID` | VARCHAR |  | The unique ID of the education point for which the status was changed. The rest of the columns in each record contain the information related to this status change. |
| 8 | `CONTACT_HX_STATUS_NAME` | VARCHAR |  | This category value is the status of the education point. The possible status entries are as follows: 1. Active 2. N/A 3. Done 4. Deleted This column is a foreign key reference to ZC_PED_CT_STATUS__PED_CT_STATUS_C. |
| 9 | `CONTACT_HX_EDIT_IN` | DATETIME (Local) |  | The date and time the education point was documented on. |
| 10 | `CONTACT_HX_USER_ID` | VARCHAR |  | The unique ID of the user who performed the documentation associated with each record in the contact-specific history. |
| 11 | `CONTACT_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `CONT_HX_TITLE_DAT` | INTEGER |  | The contact date (DAT) of the contact where the patient education history title was documented. |
| 13 | `CONT_HX_TOPIC_DAT` | INTEGER |  | The contact date (DAT) of the contact where the patient education history topic was documented. |
| 14 | `CONT_HX_POINT_DAT` | INTEGER |  | The contact date (DAT) of the contact where the patient education history point was documented. |
| 15 | `CONTACT_HX_DOC_SRC_C_NAME` | VARCHAR |  | This category value is the platform/workflow that triggered the change in the learning status of the education title, topic or point. The possible status entries are as follows: 1. Patient Education 2. Care Plan 3. Doc Flowsheet 4. Order 5. Order Set 6. Pathway 7. Task Template 8. Interface 9. Patient Assigned Task 10. Utility 11. Rover Patient Education 12. Haiku Patient Education |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |

