# CODING_CLA_ACTION_HX

> The table contains information about actions taken by users on a query (coding, Clinical Documentation Improvement, or missing doc).

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTION_USER_ID` | VARCHAR |  | Displays the IDs of all users who have taken action on the query. |
| 4 | `ACTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ACTION_UTC_DTTM` | DATETIME (UTC) |  | This item stores the corresponding time when users take action on the query. |
| 6 | `ACTION_LOCAL_DTTM` | DATETIME (Local) |  | This item stores the corresponding local time when users take action on the query. |
| 7 | `CCR_STATUS_AUDIT_C_NAME` | VARCHAR |  | Displays the action taken on the query. |
| 8 | `ACTION_ACCT_LOC_DTTM` | DATETIME (Attached) |  | The date and time of the user action in the local time zone of the location of the hospital account associated with the query. This is similar to item HNO 41082, which stores the local time zone of the location of the encounter associated with the query. Both items will store identical data except where the time zone of the encounter's location differs from the time zone of the hospital account's location. If the hospital account is combined with an account in another location, this item will be updated to the time zone of the location of the target hospital account. |
| 9 | `ACTION_END_UTC_DTTM` | DATETIME (UTC) |  | To store the instant when the current action has ended and the next action has started. |
| 10 | `ACTION_RECIP_USER_ID` | VARCHAR |  | To store the IDs of the users in the recipient list when an action was taken place by either a CDIS/Coder or a provider. In the multiple recipient case, there will be one recipient per line. |
| 11 | `ACTION_RECIP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `CCR_USR_ACTION_C_NAME` | VARCHAR |  | To store the action a user takes on a query. A query's status of completed meaning the query has been marked with an outcome of being done. |
| 13 | `CCR_USR_SUBACT_C_NAME` | VARCHAR |  | This stores the list of sub-actions that better explains the value in I HNO 41087. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

