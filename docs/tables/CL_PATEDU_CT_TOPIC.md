# CL_PATEDU_CT_TOPIC

> Enterprise reporting table for contact specific topic items in Patient Education (PED) records.

**Primary key:** `PED_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The Unique ID for the Patient Education Record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | Line count for the Patient education contact specific topic data. |
| 4 | `CONTACT_DATE` | DATETIME |  | The contact date in external format. |
| 5 | `CONTACT_TOPIC_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 6 | `CNT_TOPIC_STATUS_C_NAME` | VARCHAR |  | Category item that specifies the status of the topic. |
| 7 | `CNT_TOPIC_TITLE_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 8 | `CNT_TOPIC_KEY` | VARCHAR |  | The topic key for the contact-specific topic. It is a string in the form of Title^Topic. |
| 9 | `CNT_TOPIC_EDU_ID` | NUMERIC |  | The unique ID of the education detail record that contains additional details about this topic for this encounter. |
| 10 | `TOPIC_WAS_SUG_YN` | VARCHAR |  | Indicates whether this topic was suggested by the EMR. Y indicates that this topic was suggested by the EMR. N or null indicates that this topic was not suggested by the EMR. |
| 11 | `TOPIC_ADDED_FROM_C_NAME` | VARCHAR |  | The category ID for how this topic was added to the patient's chart. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 12 | `TOPIC_ALT_CSN_ID` | NUMERIC |  | If this topic was added to the patient's chart based on an OurPractice Advisory, then this is the unique contact serial number of the alert (ALT) contact that is used to track the firing of that OurPractice Advisory. If this topic was not added based on an OurPractice Advisory, then this is null. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |

