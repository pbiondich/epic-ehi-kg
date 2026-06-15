# IB_MEDICATION_CONCERNS

> This table stores the items used by Medication Concern In Basket messages. These include the sender, date of sending, encounter of sending, free text comment, and relevant medication.

**Primary key:** `MSG_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the in basket message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_ID` | NUMERIC | shared | The unique ID of the order associated with the In Basket message. |
| 4 | `SENDER_USER_ID` | VARCHAR |  | The unique ID of the person who sent the In Basket message. |
| 5 | `SENDER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `SENT_AT_UTC_DTTM` | DATETIME (UTC) |  | The time at which the In Basket message was sent. |
| 7 | `SENDER_COMMENT` | VARCHAR |  | The comments entered by the user who sent the message, most likely explaining why they are concerned about the patient or other relevant details regarding why sending the message is necessary. |
| 8 | `SENT_FROM_ENCOUNTER_CSN` | NUMERIC |  | The unique contact serial number of the patient encounter from which the Medication Concern message was sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |

