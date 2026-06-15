# BEN_BKT_OVRIDE

> This table stores information about benefit bucket overrides associated with AP claim service lines. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BEN_BKT_OVRD_ID` | NUMERIC |  | The unique identifier of the benefit bucket associated with the override amount. |
| 4 | `BEN_BKT_OVRD_ID_BUCKET_NAME` | VARCHAR |  | The name of the bucket. |
| 5 | `BEN_BKT_OVRD_AMT` | NUMERIC |  | Stores the benefit bucket override amount. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

