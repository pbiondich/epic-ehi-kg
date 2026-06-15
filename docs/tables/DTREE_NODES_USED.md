# DTREE_NODES_USED

> Table containing the nodes used in a decision tree run.

**Primary key:** `DTREE_ANSWER_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DTREE_ANSWER_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NODE_STATUS_C_NAME` | VARCHAR |  | Stores the status of the decision tree node based on the actions taken by the user when completing the decision tree. For example, if a user answers a question in a decision tree, the status of the question node will be set to Completed. |
| 4 | `CREATED_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The encounter ID number of the record used to store information generated as a result of the user taking an action in a decision tree. |
| 5 | `CREATED_APPT_REQUEST_ID` | NUMERIC |  | The ID number of the record used to store the appointment requests created as a result of the user taking an action in a decision tree. |
| 6 | `CHILD_DTREE_ANS_ID` | VARCHAR |  | The ID number of the record used to store the answers to a child decision tree created by a decision tree node in a decision tree. |
| 7 | `NODE_ETX_DATE_REAL` | FLOAT |  | A unique contact date in decimal format for the contact viewed by the patient during self-triage. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 references the first (or only) contact, .01 references the second contact, etc. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CREATED_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `DTREE_ANSWER_ID` | [DTREE_ANSWER](DTREE_ANSWER.md) | sole_pk | high |

