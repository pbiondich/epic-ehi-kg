# AP_CLAIM_PX_NDC

> The AP_CLAIM_PX_NDC table stores items related to National Drug Code (NDC) data for AP Claim service lines. Multiple NDCs can be associated to a single claim service line. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NDC_CODE_ID` | VARCHAR |  | The unique identifier of the National Drug Code (NDC) for the service on an AP claim. It should be used to join to NDC tables, such as RX_NDC, to find details about the code or translate to a readable format. |
| 4 | `NDC_CODE_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 5 | `NDC_QUANTITY` | NUMERIC |  | The quantity or amount of the National Drug Code (NDC) dispensed for the service on an AP claim. |
| 6 | `NDC_UNIT_C_NAME` | VARCHAR |  | The unit category ID for the quantity of a National Drug Code (NDC) dispensed for a service on an AP claim. The stored values can be translated using ZC_NDC_UNITS. |
| 7 | `NDC_PRESCRIPTIONNUM` | VARCHAR |  | The prescription number associated with the National Drug Code (NDC) dispensed for a service on an AP claim. |
| 8 | `NDC_LINK_SEQ_NUM` | VARCHAR |  | The link sequence number associated with the National Drug Code (NDC) dispensed for a service on an AP claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

