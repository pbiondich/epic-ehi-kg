# HSP_TX_LINE_INFO

> This table contains line-level transaction information from Hospital Permanent Transactions (HTR).

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account. |
| 4 | `POST_DATE` | DATETIME |  | The post date for the transaction on the hospital account. |
| 5 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `LL_REV_CODE_ID` | NUMERIC |  | This column stores the line-level revenue code for the hospital billing transaction on the hospital account. |
| 7 | `LL_REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 8 | `LL_CPT_CODE` | VARCHAR |  | This column stores the line-level CPT code for the hospital billing transaction on the hospital account. |
| 9 | `LL_MODIFIER` | VARCHAR |  | This column stores the line-level modifier info for the hospital billing transaction on the hospital account. |
| 10 | `LL_SERVICE_DATE` | DATETIME |  | This column stores the line-level service date for the hospital billing transaction on the hospital account. |
| 11 | `LL_BILLED_AMT` | NUMERIC |  | This column stores the line-level billed amount for the hospital billing transaction on the hospital account. |
| 12 | `LL_ALLOWED_AMT` | NUMERIC |  | This column stores the line-level allowed amount for the hospital billing transaction on the hospital account. |
| 13 | `LL_NOT_ALLOWED_AMT` | NUMERIC |  | This column stores the line-level not-allowed amount for the hospital billing transaction on the hospital account. |
| 14 | `LL_DED_AMT` | NUMERIC |  | This column stores the line-level deductible amount for the hospital billing transaction on the hospital account. |
| 15 | `LL_COINS_AMT` | NUMERIC |  | This column stores the line-level coinsurance amount for the hospital billing transaction on the hospital account. |
| 16 | `LL_COPAY_AMT` | NUMERIC |  | This column stores the line-level copay amount for the hospital billing transaction on the hospital account. |
| 17 | `LL_NON_COVERED_AMT` | NUMERIC |  | This column stores the line-level non-covered amount for the hospital billing transaction on the hospital account. |
| 18 | `LL_POSTED_AMT` | NUMERIC |  | This column stores the line-level posted amount for the hospital billing transaction on the hospital account. |
| 19 | `LL_ADJ_AMT` | NUMERIC |  | This column stores the line-level adjustment amount for the hospital billing transaction on the hospital account. |
| 20 | `LL_REASON_CODES` | VARCHAR |  | This column stores the line-level reason codes for the hospital billing transaction on the hospital account. |
| 21 | `LL_ACTIONS` | VARCHAR |  | This column stores the line-level action string for the hospital billing transaction on the hospital account. |
| 22 | `LL_CONTROL_NUMBER` | VARCHAR |  | This column stores the line-level control number for the hospital billing transaction on the hospital account. |
| 23 | `LL_QUANTITY` | NUMERIC |  | This column stores the line-level quantity from remittance payments. |
| 24 | `LL_CLAIM_LINE_NUMBER` | INTEGER |  | The claim line number matched with this line of the EOB. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

