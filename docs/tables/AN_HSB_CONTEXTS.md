# AN_HSB_CONTEXTS

> This table contains information about the types of contexts that have been documented on an anesthesia record. A record can be associated with a context of Anesthesia, Sedation, or Perfusion based on the activity with which a user opened the record.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the Episode. |
| 2 | `LINE` | INTEGER | PK | The line number for episode context information associated with each anesthesia record. This includes the episode context, user ID, audit time for when the context was added to the record, and whether an automatic macro was attempted. There can be multiple contexts associated with each anesthesia record, with each entry corresponding to a different line. |
| 3 | `AN_EPISODE_CONTEXT_C_NAME` | VARCHAR |  | The context that has been associated with the anesthesia record. The possible contexts include Anesthesia, Sedation, and Perfusion. |
| 4 | `RECORD_AUDIT_USER_ID` | VARCHAR |  | Stores the audit information for who caused the episode context to be added to the record. |
| 5 | `RECORD_AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `RECORD_AUDIT_UTC_DTTM` | DATETIME (UTC) |  | Stores the audit information for when the episode context was added to the record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

