# ACCOUNT_VIS_ACT_HX

> The ACCOUNT_VIS_ACT_HX table contains information about visit-level actions performed on guarantor accounts. The LINE column gives the order in which the actions happened, so rows with a higher LINE happened after rows with a lower LINE. The VIS_ACT_NUM column gives the visit number on the account.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the guarantor record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VIS_ACT_NUM` | VARCHAR |  | Visit number on the account. |
| 4 | `VIS_ACT_DATE` | DATETIME |  | The date the action happened. |
| 5 | `VIS_ACT_ACTION_C_NAME` | VARCHAR |  | The category ID that represents an action taken on a visit. |
| 6 | `VIS_ACT_CVG_ID` | VARCHAR |  | The visit coverage at the time the action happened. |
| 7 | `VIS_ACT_AMT` | NUMERIC |  | Action amount; what this amount represents is determined by the specific action taken (see VIS_ACT_ACTION_C column). Some actions (e.g. Research) may not have an amount. |
| 8 | `VIS_ACT_USER_ID` | VARCHAR |  | The unique identifier for the user record of the user who performed the action. |
| 9 | `VIS_ACT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

