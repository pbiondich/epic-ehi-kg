# AP_CLM_PX_AMBU_CERT_RM

> This table extracts the ambulance certificate condition code(s) sent at the service level for AP Claim service lines. This data should be accessed by joining to AP_CLM_PX_AMBU_CERT from AP_CLAIM_PROC_IDS on TX_ID and then to this table on TX_ID and LINE=GROUP_LINE. To report on claim service lines related to Cost Sharing Reduction (CSR), instead join through AP_CLAIM_PROC_IDS_CSR on TX_ID.

**Primary key:** `TX_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated ambulance certificate condition code(s) in this AP Claim procedure transaction record. Together with TX_ID, this forms the foreign key to the AP_CLM_PX_AMBU_CERT. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple ambulance certificate condition code(s) that are associated with the AP Claim procedure transaction records from the AP_CLM_PX_AMBU_CERT table. |
| 4 | `AMBU_CERT_COND_C_NAME` | VARCHAR |  | Stores an ambulance certificate condition code category ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

