# AP_PROC_ASSOC_DX

> This table summarizes diagnoses associated with AP claim service lines. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Primary key:** `ETR_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ETR_ID` | NUMERIC | PK | The unique ID of the AP Claim procedure transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `DX_QUAL_C_NAME` | VARCHAR | org | The diagnosis qualifier category ID associated with this procedure. |
| 5 | `DX_NUM` | INTEGER |  | The diagnosis number on the AP claim that this row corresponds to. It can be used to access diagnosis details found by joining this column on AP_CLAIM_DX.AP_DX_NUM and the known claim unique identifier on AP_CLAIM_DX.CLAIM_ID. |
| 6 | `DX_RANK` | INTEGER |  | The rank of this diagnosis compared to the other diagnoses on the service. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

