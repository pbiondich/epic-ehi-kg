# HSP_BKT_ACT_HX

> This table contains hospital liability bucket action history information from the Hospital Liability Buckets (HLB) master file.

**Primary key:** `BUCKET_ID`, `LINE`  
**Columns:** 21  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | This column stores the unique identifier for the bucket record. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. Because multiple actions can be performed on a liability bucket, each action will have a unique line number. |
| 3 | `ACTIVITY_DATE` | DATETIME |  | The date an action was recorded on a liability bucket. |
| 4 | `ACTIVITY_TYP_HA_C_NAME` | VARCHAR |  | The type of action that was recorded on a liability bucket. Examples are Claim Accepted, Transfer In, Claim Denied. |
| 5 | `TRANSFER_TYP_HA_C_NAME` | VARCHAR |  | The transfer type associated with an activity on a liability bucket. Transfer types are Charge, Payment, Adjustment, and Balance. |
| 6 | `DENIAL_CODE_ID` | VARCHAR |  | A claim denial code associated with a claim denied action that was recorded on a liability bucket. |
| 7 | `DENIAL_CODE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 8 | `ACTIVITY_AMOUNT` | NUMERIC |  | The monetary amount associated with an action that was recorded on a liability bucket. |
| 9 | `ACTIVITY_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user who performed an action that was recorded on a liability bucket. |
| 10 | `ACTIVITY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `SOURCE_BUCKET_ID` | NUMERIC |  | The liability bucket that is considered the source for this liability bucket. A source liability bucket is a bucket out of which transactions are transferred into another bucket. |
| 12 | `TARGET_BUCKET_ID` | NUMERIC |  | The liability bucket that is considered the target for this liability bucket. A target liability bucket is a bucket into which transactions are transferred from another bucket. |
| 13 | `BALANCE_AFTER` | NUMERIC |  | The balance on a liability bucket after an action was performed on it. |
| 14 | `NEW_BKT_STS_HA_C_NAME` | VARCHAR |  | The status of a liability bucket after an action was performed on it. |
| 15 | `ACTIVITY_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 16 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account with which the liability bucket is associated. |
| 17 | `EXT_DENIAL_CODE` | VARCHAR |  | External claim denial code associated with a claim denied action that was recorded on the liability bucket. |
| 18 | `GRP_CODE_C_NAME` | VARCHAR | org | Reason group code associated with the denial code that was recorded on a liability bucket. |
| 19 | `ACTIVITY_DTTM` | DATETIME (Local) |  | The column returns the instant an action was recorded on a liability bucket. |
| 20 | `ACTIVITY_CONTEXT_C_NAME` | VARCHAR |  | The column stores the context for the action on a given liability bucket. |
| 21 | `ACTIVITY_SRC_C_NAME` | VARCHAR |  | The column stores the source of an activity for a given liability bucket. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

