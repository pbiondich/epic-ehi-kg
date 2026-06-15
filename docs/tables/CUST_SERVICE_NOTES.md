# CUST_SERVICE_NOTES

> The CUST_SERVICE_NOTES table contains information about the notes that are attached to each customer service communication.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique ID of the note attached to a customer service communication. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTE_DATE` | DATETIME |  | The date when the note was created. This column contains date information only. Column NOTE_DATETIME holds date and time information. |
| 4 | `NOTE_USER_ID` | VARCHAR |  | The unique ID of the user who created the note. |
| 5 | `NOTE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `RECORD_ID` | NUMERIC | shared | The unique identifier for the customer service communication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

