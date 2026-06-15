# AP_CLM_PX_AMBU_CERT

> This table is used in conjunction with AP_CLM_PX_AMBU_CERT_RM to determine ambulance certificate condition codes sent at the service level for AP Claims. Each line for a TX_ID in this table corresponds to the group line for the same TX_ID in the AP_CLM_PX_AMBU_CERT_RM table. Conditions in that table are grouped to either a yes, no, or response code in this table. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AMBU_YN_COND_YN` | VARCHAR |  | Indicates whether or not the related condition codes apply to the service. Y is stored if they apply, and N if not. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

