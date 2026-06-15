# FOLLOW_UP_TOPICS

> This table contains information regarding patient outreach topics, patients for which outreach was performed on these topics, who performed the outreach and when the outreach was done. The records included in this table are LFT records that are designated as clincal outreach tracking records.

**Primary key:** `FOLLOW_UP_ID`  
**Columns:** 13  
**Org-specific columns:** 1  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FOLLOW_UP_ID` | NUMERIC | PK | The unique identifier (.1 item) for the record. |
| 2 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `FOLLOW_UP_DTTM` | DATETIME (UTC) |  | This column displays the instant of patient outreach. |
| 5 | `FOLLOW_UP_TOPIC_C_NAME` | VARCHAR | org | This column displays patient outreach topics such as Diabetes or Hypertension. |
| 6 | `FOLLOW_UP_USER_ID` | VARCHAR |  | This column displays the user who performed the patient outreach action. This column is frequently used to link to the CLARITY_EMP table. |
| 7 | `FOLLOW_UP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `FOLLOW_UP_NEXT_DT` | DATETIME |  | This column displays the date when the patient will next require outreach. |
| 9 | `LINKED_CSN_ID` | NUMERIC |  | This item contains a pointer to the encounter linked with this outreach. |
| 10 | `PAT_OUT_SOURCE_C_NAME` | VARCHAR |  | Stores the source of the patient outreach |
| 11 | `MAIL_LETTER_NUM` | INTEGER |  | This contains the line in SI EPT 20200 which contains the details of the letter. |
| 12 | `PHONE_MSG_ID` | VARCHAR |  | This item stores the pointer to the In Basket message that is sent out to support staff asking them to call patients. |
| 13 | `PAT_PORTAL_MESSAGE_ID` | VARCHAR |  | This item stores a pointer to the MyChart message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [FOLLOW_UP_ACTIONS](FOLLOW_UP_ACTIONS.md) | `FOLLOW_UP_ID` | high |

