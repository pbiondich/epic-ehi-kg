# HSP_BKT_ICN

> This table holds information about claim internal control numbers (ICNs) on Hospital Liability Buckets (HLB) records for Resolute Hospital Billing.

**Primary key:** `BUCKET_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the bucket record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ICN_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The instant in which the new internal control number (ICN) is added. |
| 4 | `ICN_UPDATE_USER_ID` | VARCHAR |  | The user who added an internal control number (ICN) to the bucket |
| 5 | `ICN_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CLAIM_ICN` | VARCHAR |  | The internal control number (ICN) associated with this bucket. |
| 7 | `ICN_SOURCE_PMT_TX_ID` | NUMERIC |  | The payment transaction that is the source of the internal control number (ICN) on this bucket. |
| 8 | `ICN_SOURCE_CLAIM_RECON_ID` | VARCHAR |  | The claim reconciliation data that is the source of the internal control number (ICN) on the bucket |
| 9 | `ICN_COMMENT_REF_NUM` | VARCHAR |  | The comment or reference number associated with the internal control number (ICN) update. |
| 10 | `ICN_SOURCE_C_NAME` | VARCHAR |  | The external source of the internal control number (ICN) on this bucket. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

