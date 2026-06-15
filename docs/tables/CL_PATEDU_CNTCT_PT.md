# CL_PATEDU_CNTCT_PT

> Enterprise reporting table for Contact specific point items in Patient education record.

**Primary key:** `PED_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The Unique ID for the Patient Education Record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | Line count for the Patient education point. This is contact specific. |
| 4 | `CONTACT_DATE` | DATETIME |  | The contact date in external format. |
| 5 | `CONTACT_POINT_ID` | VARCHAR |  | The unique identifier for education point for the patient education contact. |
| 6 | `CNT_POINT_TOPIC_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 7 | `CNT_POINT_TITLE_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 8 | `CNT_POINT_KEY` | VARCHAR |  | The education point key for contact-specific history. This is a string in the form of Title^Topic^Point. |
| 9 | `CNT_POINT_STATUS_C_NAME` | VARCHAR |  | Status of the patient education point. A category item. |
| 10 | `CNT_POINT_IED_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 11 | `CNT_MYPOINT_HNO_ID` | VARCHAR |  | Unique identifier for the note associated with the My Point. My Point is created on the fly and this ID, together with the contact date (DAT), can be used to link to the associated note. |
| 12 | `CNT_MYPOINT_HNO_DA` | VARCHAR |  | Contact date for the note associated with the My Point. My Point is created on the fly and this contact date (DAT), together with the note (HNO) ID, can be used to link to the associated note. |
| 13 | `CNT_POINT_EDU_ID` | NUMERIC |  | The unique ID of the education detail record that contains additional details about this point for this encounter. |
| 14 | `POINT_WAS_SUG_YN` | VARCHAR |  | Indicates whether this point was suggested by the EMR. Y indicates that this point was suggested by the EMR. N or null indicates that this point was not suggested by the EMR. |
| 15 | `POINT_ADDED_FROM_C_NAME` | VARCHAR |  | The category ID for how this point was added to the patient's chart. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 16 | `POINT_ALT_CSN_ID` | NUMERIC |  | If this point was added to the patient's chart based on an OurPractice Advisory, then this is the unique contact serial number of the alert (ALT) contact that is used to track the firing of that OurPractice Advisory. If this point was not added based on an OurPractice Advisory, then this is null. |
| 17 | `CNCT_FIRST_DOSE_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |

