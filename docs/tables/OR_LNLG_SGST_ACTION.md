# OR_LNLG_SGST_ACTION

> Stores the actions performed on a set of surgical procedure suggestions.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SUGGESTION_ACTION_C_NAME` | VARCHAR |  | This item stores the actions performed on a set of LLM surgical procedure suggestions. |
| 4 | `ACTION_UTC_DTTM` | DATETIME (UTC) |  | This item stores the UTC instant at which an action was performed on a set of LLM procedure suggestions. |
| 5 | `ACTION_USER_ID` | VARCHAR |  | This item stores the user who performed an action on a set of LLM surgical procedure suggestions. |
| 6 | `ACTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

