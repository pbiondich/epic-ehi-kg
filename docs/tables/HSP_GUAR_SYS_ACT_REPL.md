# HSP_GUAR_SYS_ACT_REPL

> This table contains hospital guarantor system action history information.

**Primary key:** `GUAR_ACCOUNT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GUAR_ACCOUNT_ID` | NUMERIC | PK | This column stores the unique identifier for the guarantor record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SYSTEM_ACTION_C_NAME` | VARCHAR |  | The system action category ID. |
| 4 | `ACTION_DATE` | DATETIME |  | The date of the system action. |
| 5 | `ACTION_DATA` | VARCHAR |  | The data for the system action. |
| 6 | `ACTION_COMMENT` | VARCHAR |  | The comment for the system action. |
| 7 | `IS_SYS_ACT_SUCC_YN` | VARCHAR |  | This column stores whether the system action is successful. |
| 8 | `ACTION_UTC_DTTM` | DATETIME (UTC) |  | The instant when the system action was attempted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

