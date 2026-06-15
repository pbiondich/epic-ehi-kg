# MYC_MESG_CNCL_RSN

> The MYC_MESG_CNCL_RSN table contains information about Secure Patient Message records sent to request the cancellation of an appointment. Specifically patients can enter comments on the reason for their cancellation request. This table allows you to report on those free text comments.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique identifier for the message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CANCEL_REASON` | VARCHAR |  | The reason the patient is requesting cancellation of an appointment. This field will only be populated for appointment cancellation request messages and if the patient is required or chose to write an explanation as to why they are requesting cancellation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

