# EDIT_CLM_GEN

> This table stores claim edit generation information.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `EC_GEN_USER_ID` | VARCHAR |  | Stores the user ID of the person who performed edit operations. |
| 4 | `EC_GEN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `EC_GEN_INST_DTTM` | DATETIME (Local) |  | Stores the date/time instance when the claim was edited. |
| 6 | `EC_GEN_NUM_LNS` | INTEGER |  | Stores the total number audit lines for the claim edit operation. |
| 7 | `EC_GEN_START_LN` | INTEGER |  | Stores the line number from where the audit starts for a particular claim edit. |
| 8 | `EC_GEN_NUM_AUDIT` | INTEGER |  | Stores the claim edit generation number for the audit. |
| 9 | `EC_GEN_START_AUDIT` | INTEGER |  | Stores the claim edit generation start audit number. |
| 10 | `EC_GEN_TYP_C_NAME` | VARCHAR |  | This item distinguishes initial values, user edited values, and values reset from edited back to system calculated values. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

