# MYC_MESG_RECIPIENTS_OUT

> This table stores the list of out of contact message recipients. This includes the dates that their out of contact event started and ended.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RECIPIENT_USER_ID` | VARCHAR |  | Out of contact message recipients. |
| 4 | `RECIPIENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `RECIPIENT_START_DATE` | DATETIME |  | The start date for the message recipients out of contact occasion. |
| 6 | `RECIPIENT_END_DATE` | DATETIME |  | The end date for the message recipients out of contact occasion. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

