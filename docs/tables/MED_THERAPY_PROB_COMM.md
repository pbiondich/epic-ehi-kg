# MED_THERAPY_PROB_COMM

> This table contains the communications associated with a recommendation related to a medication therapy problem.

**Primary key:** `PROBLEM_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the Medication Therapy Problem record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `MTP_RECOMMENDATION_LINE` | INTEGER |  | The medication therapy problem recommendation associated with this communication. |
| 5 | `MTP_COMM_DIRECTION_C_NAME` | VARCHAR |  | The directionality of the communication that has been sent associated with the medication therapy recommendation. |
| 6 | `MTP_COMMUNICATION_TYPE_C_NAME` | VARCHAR |  | The type of communication that is associated with the medication therapy problem. |
| 7 | `COMMUNICATION_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores a CSN reference to the encounter where the medication therapy problem communication was sent. |
| 8 | `COMMUNICATION_JOB` | VARCHAR |  | This item stores the job ID (I EPT 19749) of the communication in Encounter Communication related group 19730 in the EPT master file. Replies via InBasket will share the same job ID. |
| 9 | `COMMUNICATION_CREATED_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant the medication therapy problem communication was sent. |
| 10 | `MTP_COMM_PROV_ISSUE_C_NAME` | VARCHAR | org | The category ID of the issue documented by the provider to explain why they are declining or modifying the recommendation. |
| 11 | `MTP_COMM_PROV_COMMENT` | VARCHAR |  | The medication therapy recommendation comments entered by the provider to explain why they declined or modified the recommendation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COMMUNICATION_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

