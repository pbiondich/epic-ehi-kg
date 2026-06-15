# AP_CLAIM_PROC_5

> This table summarizes data for AP Claims service lines, with each service line given one row. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Overflow of:** [AP_CLAIM_PROC](AP_CLAIM_PROC.md)  
**Primary key:** `TX_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `PRIMARY_PAYER_CODE` | VARCHAR |  | The code specifying a federal non-Medicare program or other source that has primary responsibility for the payment of the Medicare beneficiary's medical bills relating to the service line on the claim. The presence of this code indicates that some other payer besides Medicare covered at least some portion of the charges. |
| 3 | `HCPCS_BETOS_CODE` | VARCHAR |  | The Berenson-Eggers Type of Service (BETOS) classification assigned to the Healthcare Common Procedure Coding System (HCPCS) code for the service line. |
| 4 | `FEDERAL_SERVICE_CODE` | VARCHAR |  | Code indicating the type of service, as defined in the CMS Medicare Carrier Manual, for this service line on the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

