# HSP_CLP_PMT_CLASS

> This table contains the payment classification information for the claim print records associated with the hospital account/liability bucket.

**Primary key:** `CLAIM_PRINT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 26  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the claim print record associated with a single hospital account/bucket. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The date of this contact in calendar format. |
| 3 | `LINE` | INTEGER | PK | The line number of the associated claim in the related payment classification group. |
| 4 | `PC_TYPE_C_NAME` | VARCHAR |  | The payment classification type of the associated claim in the related revenue code group (e.g. 1 - Ambulatory Payment Classification, 2 - Home Health, 3 - CPT). |
| 5 | `PC_CODE` | VARCHAR |  | The payment classification code of the associated claim in the related revenue code group. |
| 6 | `PC_STATUS_IND_C_NAME` | VARCHAR |  | This column stores the payment classification status indicator of the associated claim in the related revenue code group (e.g. 1 - significant procedures, 2 - surgical services, 3 - medical visits, 4 - ancillary services, 5 - partial hospitalization, 6 - incidental services, etc.). |
| 7 | `PC_ORIG_AMT` | NUMERIC |  | The original (dollar) amount of the claim. |
| 8 | `PC_EXP_AMT` | NUMERIC |  | The expected (dollar) amount of the claim. |
| 9 | `PC_ASSOC_CLM_LINE` | INTEGER |  | The associated claim line for the payment classification. |
| 10 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account with which this claim is associated. |
| 11 | `CM_PHY_OWN_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this Chronicles record. This is populated only if you use IntraConnect. |
| 12 | `PC_APG_TYPE` | VARCHAR |  | This column stores the payment classification ambulatory payment group (APG) type. |
| 13 | `PC_APG_CATEGORY` | VARCHAR |  | This column stores the payment classification APG category. |
| 14 | `PC_MUL_SIG_PRO_YN` | VARCHAR |  | Stores the multiple significant procedure discount flag |
| 15 | `PC_REP_ANCILL_YN` | VARCHAR |  | Stores the repeat ancillary discount flag |
| 16 | `PC_BILAT_PRO_YN` | VARCHAR |  | Stores the bilateral procedure discount flag |
| 17 | `PC_TERMIN_PR_YN` | VARCHAR |  | Stores the terminated procedure discount flag |
| 18 | `PC_ADJUSTED_WEIGHT` | NUMERIC |  | This column stores the adjusted APG weight. |
| 19 | `PC_PAYMENT_ACTION` | VARCHAR |  | Stores the payment classification payment action |
| 20 | `PC_ADDON_PAYMENT` | NUMERIC |  | Stores the payment classification capital add-on payment |
| 21 | `PC_APG_PAYMENT` | NUMERIC |  | This column stores the payment classification APG payment. |
| 22 | `PC_BLENDED_PAYMENT` | NUMERIC |  | Stores the payment classification blended payment |
| 23 | `PC_EXISTING_PAYMENT` | NUMERIC |  | Stores the payment classification payment calculated using existing system during transition to APG based reimbursement system |
| 24 | `PC_PMT_CLASS_WT` | NUMERIC |  | Stores payment classification weight |
| 25 | `PC_COMPOSITE_LINES` | VARCHAR |  | This item stores extra information to identify special characteristics of this line of Ambulatory Payment Classification (APC) data. This item will be populated only if the claim has its APC grouping source configured to use the APC grouping framework. This item may be populated with one or more of the following separated by a pipe delimiter (\|). |
| 26 | `PC_GRP_MTHD_C_NAME` | VARCHAR | org | Holds the grouping method that this line was created from. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

