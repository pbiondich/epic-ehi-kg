# CV_NO_COMPLICATIONS

> Table to keep track of "no complications".

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NO_COMPLICATIONS_YN` | VARCHAR |  | Item to keep track that there were no complications. |
| 4 | `NO_COMP_USER_ID` | VARCHAR |  | Item to keep track the user that modified "no complications". |
| 5 | `NO_COMP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `NO_COMP_EDIT_TIME_DTTM` | DATETIME (Attached) |  | Item to keep track the time "no complications" was modified. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

