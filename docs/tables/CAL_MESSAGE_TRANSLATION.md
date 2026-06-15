# CAL_MESSAGE_TRANSLATION

> This table contains the original native language version of a message that was sent to a patient or patient's visitor, if it was translated into the recipient's target language.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MESSAGE_TRANSLATED_TEXT` | VARCHAR |  | This item stores the original native-language version of the body of text sent to the recipient, if the message was translated into the recipient's preferred language. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

