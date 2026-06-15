# HSP_BUCKET_2

> This table contains hospital liability bucket information from the Hospital Liability Buckets (HLB) master file. This table does not include information for pre-allocated HLB records that are not yet in use.

**Overflow of:** [HSP_BUCKET](HSP_BUCKET.md)  
**Primary key:** `BUCKET_ID`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the bucket record. |
| 2 | `TIMELY_FILING_DATE` | DATETIME |  | The timely filing deadline date for insurance buckets. This is blank for Late Write Off and Supplemental Payment Claim buckets. |
| 3 | `REPLACEMENT_TIMELY_FILING_DATE` | DATETIME |  | The replacement timely filing deadline date for insurance buckets. This is blank for Late Write Off and Supplemental Payment Claim buckets. |
| 4 | `AR_CLASSIFICATION_C_NAME` | VARCHAR |  | This column stores the A/R classification of this bucket. |
| 5 | `BUCKET_CLAIM_STATUS_C_NAME` | VARCHAR |  | The current claim status associated with the claim status update for the accepted claim on the bucket. |
| 6 | `BUCKET_AR_STATUS_C_NAME` | VARCHAR |  | A status for the bucket with detail about which stage of the billing cycle the AR is at. |
| 7 | `CURRENT_CLAIM_PRINT_ID` | NUMERIC |  | The current active claim that is associated with the bucket. If the bucket has multiple active claims, this value will be the first claim. |
| 8 | `TOTAL_REFUND_AMT` | NUMERIC |  | The total refund amount for the bucket. |
| 9 | `TOTAL_ADJ_EXCL_REFUND_AMT` | NUMERIC |  | The total adjustment amount for the bucket, excluding refunds. |
| 10 | `CONTRACTUALIZED_STS_C_NAME` | VARCHAR |  | The current contractualized status of the bucket. |
| 11 | `POSTED_NA_WOFF_AMT` | NUMERIC |  | The monetary amount that has been posted as a contractual not-allowed write-off to the bucket. The amount is calculated based on the adjustments posted to the bucket. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

