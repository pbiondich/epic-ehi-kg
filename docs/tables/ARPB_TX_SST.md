# ARPB_TX_SST

> Sliding Scale Table Related Items for Transactions. This table has information that is populated by sliding scale workflows and by self-pay discount workflows.

**Primary key:** `TX_ID`  
**Columns:** 17  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `SST_DISC` | INTEGER |  | This field holds the percentage amount of the sliding scale discount. |
| 3 | `SST_OVERRIDE` | VARCHAR |  | This item is a Yes/No flag that stores whether the system increases the self-pay amount due to the application of a minimum fee. |
| 4 | `ORIGINAL_PAT_PORT` | NUMERIC |  | The original self-pay portion before the amount was reduced according to the sliding scale. |
| 5 | `SLIDING_MIN_FEE` | NUMERIC |  | This is the minimum fee that is associated with this transaction. This applies only to sliding scale and not self-pay discount. |
| 6 | `SST_WO` | NUMERIC |  | This is the amount of the write-off that was applied. |
| 7 | `SST_DEFAULT_YN` | VARCHAR |  | Indicates whether the sliding scale table system calculation was overridden by a user. Y indicates that the sliding scale table system calculation was overridden. N indicates that it was not. |
| 8 | `SST_DISC_OV_YN` | VARCHAR |  | Indicates whether the discount amount was overridden by a user. Y indicates that discount amount was overridden. N indicates that it was not. |
| 9 | `SST_DISC_APP_YN` | VARCHAR |  | Indicates whether a sliding scale discount has been applied to this transaction. |
| 10 | `SST_SELF_OVRD_YN` | VARCHAR |  | Indicates whether the self-pay portion in the self-pay discount workflow was overridden by a user. Y indicates that self-pay portion was overridden. N indicates that it was not. |
| 11 | `SST_FF_APPLIED_YN` | VARCHAR |  | This item holds a flag to determine if a flat fee discount was applied to this transaction. |
| 12 | `SST_FF_PROC_YN` | VARCHAR |  | This item holds a flag to determine if the procedure associated with this charge is a flat fee eligible procedure. |
| 13 | `SST_WO_APPLIED_YN` | VARCHAR |  | This item is a flag that is set to Yes if a Sliding Scale Write off adjustment has been applied to this charge. |
| 14 | `FF_WO_APPLIED_YN` | VARCHAR |  | This item holds a flag to determine if a flat fee discount was applied to this transaction. |
| 15 | `DISCOUNT_TYPE_C_NAME` | VARCHAR | org | Indicates what kind of discount was used. This item only applies to self-pay discount. The choices are percentage or fee schedule. |
| 16 | `SSCALE_PCT` | INTEGER |  | This field holds the sliding scale write-off percentage. |
| 17 | `SP_DISC_EXCL_RS_C_NAME` | VARCHAR |  | This item stores the self-pay discount exclusion reason: 1 - Self-pay amount is manually overridden by user 2 - Procedure is excluded from self-pay discount 3 - Waiting for all charges on the visit to NRP to self-pay |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

