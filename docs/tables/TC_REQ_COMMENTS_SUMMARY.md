# TC_REQ_COMMENTS_SUMMARY

> Contains information about Transfer Center notes.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TC_REQUEST_COMMENT_TEXT` | VARCHAR |  | Free text information that can be documented for a transfer center request |
| 4 | `TC_REQ_COMMENT_INST_UTC_DTTM` | DATETIME (UTC) |  | When a user documents information in the free text note, this item will store the timestamp of when it was edited. |
| 5 | `TC_REQUEST_COMMENT_USER_ID` | VARCHAR |  | When a user edits a Transfer Center request's free text information, this will store what user made the edit. |
| 6 | `TC_REQUEST_COMMENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

