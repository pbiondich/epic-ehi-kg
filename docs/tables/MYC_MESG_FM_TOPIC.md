# MYC_MESG_FM_TOPIC

> This table contains information about family medical history submitted by the patient in a history questionnaire.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The ID of the web-based chart system message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FAM_TOPIC_ID` | VARCHAR |  | The ID of the family history topic in the history questionnaire submitted by the patient. |
| 4 | `FAM_TOPIC_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |
| 5 | `FAM_TOPIC_PROB_C_NAME` | VARCHAR | org | The category value of the problem entered by the patient when answering a family history questionnaire. |
| 6 | `FAM_TOPIC_REL_C_NAME` | VARCHAR | org | The relation type of the family member entered by the patient in a family history questionnaire. |
| 7 | `FAM_TOPIC_NAME` | VARCHAR |  | The name of the family member entered by the patient in a family history questionnaire. |
| 8 | `FAM_TOPIC_CMT` | VARCHAR |  | The comment entered by the patient for a family history topic in a family history questionnaire. |
| 9 | `FAM_TOPIC_UNCHKD_YN` | VARCHAR |  | This column stores the problem status - checked or unchecked by the patient in MyChart. |
| 10 | `FAM_TOPIC_FILED_YN` | VARCHAR |  | The filed status of the family history topic--has the provider filed it to the patient's record. |
| 11 | `FAM_TOPIC_REL_ID` | VARCHAR |  | Stores the unique relationship of a family member. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

