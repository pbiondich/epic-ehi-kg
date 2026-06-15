# CUST_SVC_MYC_LETTER_AUDIT

> This table contains the history of when Customer Relationship Management (CRM) letters were released to the patient portal or retracted from the patient portal.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique ID of the communication record that the audit trail is for. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LETTER_AUD_NOTE_ID` | VARCHAR |  | The unique ID of the note that was released or unreleased from the patient portal. |
| 4 | `LETTER_AUD_USER_ID` | VARCHAR |  | The unique ID of the user that released or unreleased the letter from the patient portal. |
| 5 | `LETTER_AUD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `LETTER_ACTION_C_NAME` | VARCHAR |  | The category ID for an action that indicates if the letter was released to or removed from the patient portal. |
| 7 | `CHANGE_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the letter was released or unreleased from the patient portal. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

