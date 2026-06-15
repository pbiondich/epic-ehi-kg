# AP_CLAIM_PROV_RESP

> This table contains the provider responsibility information for AP Claim procedures. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `LINE` | INTEGER | PK | The line number of the provider responsibility for this transaction record. |
| 3 | `PROV_RESP_AMT` | NUMERIC |  | The dollar amount for a specific provider responsibility. |
| 4 | `PRV_RESP_SRC_TP_C_NAME` | VARCHAR |  | The type of provider responsibility. |
| 5 | `EOB_CODE_ID_EOB_CODE_NAME` | VARCHAR |  | The name of the processing code. |
| 6 | `PROV_RESP_OVRD_AMT` | NUMERIC |  | The user-entered override to the dollar amount a specific provider responsibility. If present, the value in this column overrides the value in PRV_RESP_AMT. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

