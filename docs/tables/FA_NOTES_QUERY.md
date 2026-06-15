# FA_NOTES_QUERY

> This table contains information about queries sent to retrieve financial information for patients and/or patient contacts in a financial assistance case record.

**Primary key:** `NOTE_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `QUERY_PERSON_USER_ID` | VARCHAR |  | The unique ID associated with the user record who triggered the query. This column is frequently used to link to the CLARITY_EMP table. |
| 3 | `QUERY_PERSON_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 4 | `QUERY_DATE` | DATETIME |  | The date when the query was triggered. |
| 5 | `QUERY_TRIGGER_SOURCE_C_NAME` | VARCHAR |  | The trigger source category ID for the query. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

