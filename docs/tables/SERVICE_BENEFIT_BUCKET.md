# SERVICE_BENEFIT_BUCKET

> This table stores benefit bucket information relevant to or caused by AP Claim service lines. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BENEFIT_BUCKET_ID` | NUMERIC |  | Stores the unique identifier of the benefit bucket affected by this service. |
| 4 | `BENEFIT_BUCKET_ID_BUCKET_NAME` | VARCHAR |  | The name of the bucket. |
| 5 | `BENEFIT_BUCKET_MAX` | NUMERIC |  | Stores the maximum number of units allowed for this benefit bucket level. |
| 6 | `BENEFIT_BUCKET_USED` | NUMERIC |  | Stores the number of units used for this benefit bucket level. |
| 7 | `BENEFIT_BCKT_REMAIN` | NUMERIC |  | Stores the number of units remaining for this benefit bucket level. |
| 8 | `BUCKET_LEVEL` | VARCHAR |  | Stores the benefit bucket level used. |
| 9 | `BENEFIT_BUCKET_COMPUTED` | NUMERIC |  | The original amount that the system computed to be accumulated to the bucket. |
| 10 | `ROLL_PRD_STR` | VARCHAR |  | The roll period that the benefit bucket accumulation used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

