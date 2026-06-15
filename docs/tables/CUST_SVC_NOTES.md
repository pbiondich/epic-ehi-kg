# CUST_SVC_NOTES

> The CUST_SVC_NOTES table contains information about the notes that are attached to each customer service communication.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier for the customer service communication. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTE_ID` | VARCHAR | shared | The unique ID of the note attached to a customer service communication. |
| 4 | `NOTE_DTTM` | DATETIME (Local) |  | The date and time when the note was created. |
| 5 | `NOTE_USER_ID` | VARCHAR |  | The unique ID of the user who created the note. |
| 6 | `NOTE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

