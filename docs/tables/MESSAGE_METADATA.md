# MESSAGE_METADATA

> Stores message metadata for MedCom messages.

**Primary key:** `COMMUNICATION_ID`  
**Columns:** 4  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMMUNICATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the routing record. |
| 2 | `MESSAGE_CAT_LETTER_REASON_C_NAME` | VARCHAR | org | Stores the Category for the message. |
| 3 | `MESSAGE_SUBJECT_C_NAME` | VARCHAR | org | The message subject stored as a discrete option. |
| 4 | `MESSAGE_SUBJECT_STR` | VARCHAR |  | The message's subject, stored as a free-text entry |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

