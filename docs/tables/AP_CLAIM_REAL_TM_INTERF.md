# AP_CLAIM_REAL_TM_INTERF

> This table contains data for each service line from the real time claims interface such as ethical price, contract adjustment, and provider discount. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Primary key:** `TX_ID`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `ETHICAL_PRICE` | NUMERIC |  | This column stores the ethical price for the service line. |
| 3 | `CONTRACT_ADJ` | NUMERIC |  | This column stores the contract adjustment for the service line. |
| 4 | `MMAP_PRICE` | NUMERIC |  | This column stores the maximum medical aid price (MMAP) for the service line. |
| 5 | `MMAP_ADJ` | NUMERIC |  | This column stores the maximum medical aid price (MMAP) adjustment for the service line. |
| 6 | `BULK_BREAK_ADJ` | NUMERIC |  | This column stores the bulk break adjustment for the service line. |
| 7 | `PROVIDER_DISCOUNT` | NUMERIC |  | This column stores the provider discount for the service line. |
| 8 | `ADMINISTRATIVE_FEE` | NUMERIC |  | This column stores the administrative fee for the service line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

