# OR_LNLG_SGST_FEEDBACK

> This table stores user feedback about LLM surgical procedure suggestions.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FEEDBACK_USER_ID` | VARCHAR |  | This item stores the list of user (EMP) records who have left feedback on the results of an LLM query regarding surgical procedure suggestions. |
| 4 | `FEEDBACK_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `FEEDBACK_STATUS_C_NAME` | VARCHAR |  | This item stores the type of feedback that a user left on the results of an LLM query regarding surgical procedure suggestions. |
| 6 | `FEEDBACK_REASON_C_NAME` | VARCHAR |  | This item stores the reason that a user selected for why they left negative on the results of an LLM query regarding surgical procedure suggestions. |
| 7 | `FEEDBACK_COMMENT` | VARCHAR |  | This item stores the comment that a user left when submitting negative feedback on the results of an LLM query regarding surgical procedure suggestions. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

