# VALUE_EDIT_HISTORY

> All values associated with a claim are stored in the Claim External Value record. The VALUE_EDIT_HISTORY table holds the dates and times of all changes to the claim.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `USER_EDIT_INST_DTTM` | DATETIME (UTC) |  | The Coordinated Universal Time (UTC) date and time of the user's edit session. |
| 4 | `USER_EDIT_TYP_C_NAME` | VARCHAR |  | This item holds the type of information in the edit - initial values or user edits. |
| 5 | `USER_EDIT_ID` | VARCHAR |  | This item holds the user ID who performed the edit. |
| 6 | `USER_EDIT_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `USER_EDIT_CMT` | VARCHAR |  | This item holds a comment entered by the user describing the edit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

