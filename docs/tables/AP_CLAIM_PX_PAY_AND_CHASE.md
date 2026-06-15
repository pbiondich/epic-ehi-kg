# AP_CLAIM_PX_PAY_AND_CHASE

> This table contains the pay and chase history for AP Claim procedures.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PC_HISTORY_PROGRAM_C_NAME` | VARCHAR | org | This item stores the pay and chase program that the service line was extracted for. |
| 4 | `PC_HISTORY_AMOUNT` | NUMERIC |  | This item stores the chase amount for the specified pay and chase program that a service line was extracted for. |
| 5 | `PC_HISTORY_INST_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant that the service line was extracted for a pay and chase program. |
| 6 | `PC_HISTORY_AP_PC_ACTION_C_NAME` | VARCHAR |  | This item stores the pay and chase action that was taken on the service line. |
| 7 | `PC_HIST_COMMENT` | VARCHAR |  | This item stores the comment associated with the pay and chase action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

