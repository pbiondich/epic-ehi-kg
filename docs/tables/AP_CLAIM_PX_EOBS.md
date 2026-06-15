# AP_CLAIM_PX_EOBS

> This table contains each Explanation of Benefits (EOB) code attached to AP Claim service lines. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EOB_CODE_ID_EOB_CODE_NAME` | VARCHAR |  | The name of the processing code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

