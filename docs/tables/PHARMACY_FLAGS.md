# PHARMACY_FLAGS

> Pharmacy flags on the order. Flags are used by Ambulatory Pharmacy to mark fill requests as needing additional review. There are various types of flags, and one or more can be added to specific fill request contacts on the order.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order that has pharmacy flags attached to it. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `PHARMACY_FLAG_ID` | NUMERIC |  | The unique ID of the flag that is attached to this order. |
| 7 | `PHARMACY_FLAG_ID_RECORD_NAME` | VARCHAR |  | The flag name. |
| 8 | `INSTANT_ADDED_DTTM` | DATETIME (UTC) |  | The instant when this flag was added to the order. |
| 9 | `ADDED_BY_USER_ID` | VARCHAR |  | The unique identifier for the user that added the flag to the order. |
| 10 | `ADDED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `FLAG_BLOCKING_YN` | VARCHAR |  | Indicates if the flag is blocking this order from continuing past a certain point in the workflow. 'Y' indicates that the flag is blocking. 'N' or NULL indicate that the flag is not blocking. |
| 12 | `ASSOCIATED_CVG_ID` | NUMERIC |  | The unique identifier for the coverage that is associated with this flag. |
| 13 | `FREE_TXT_DESC` | VARCHAR |  | A free text description of what the flag indicates. |
| 14 | `FLAG_COMMENT_ID` | VARCHAR |  | The unique identifier of the notes record that contains the text that the user added to the customer flag. |
| 15 | `FLAGGING_PHR_ID` | NUMERIC |  | The unique identifier for the pharmacy record that added the flag |
| 16 | `FLAGGING_PHR_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 17 | `RX_FLG_ADD_RSN_C_NAME` | VARCHAR | org | The flag added reason category ID for the order. |
| 18 | `FOLLOW_UP_DATE` | DATETIME |  | The date the flag should be deferred until. For Charging flags, the follow-up date is when the fill should be re-adjudicated. |
| 19 | `FLAG_QUESR_ANSWER_ID` | VARCHAR |  | This item contains the questionnaire answers associated with the pharmacy patient-facing flag. When a patient submits a questionnaire in MyChart from the patient-facing flag banner, the questionnaire answer record (HQA) is stored in this item. This is the patient's answers to the questionnaire stored in I ORD 47740. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

