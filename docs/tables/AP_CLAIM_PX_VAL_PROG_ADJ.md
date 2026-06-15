# AP_CLAIM_PX_VAL_PROG_ADJ

> This table contains the payment adjustments from value-based programs for AP Claim procedures. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMPUTED_PROGRAM_ADJ` | NUMERIC |  | The value-based program adjustment amount for the procedure, as computed by the system. |
| 4 | `OVERRIDE_PROGRAM_ADJ` | NUMERIC |  | The value-based program adjustment amount for the procedure, as overridden by the user. |
| 5 | `PROGRAM_ADJ_COMMENT` | VARCHAR |  | The value-based program payment adjustment comment entered by the system when calculating the adjustment or by a user when overriding the adjustment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

