# PR_EST_ADDL_INFO

> Contains additional information related to a price estimate, such as tax and discount amounts.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 25  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | This column stores the unique identifier for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SURCHARGE_AMT` | NUMERIC |  | The estimated surcharge amount. |
| 4 | `SYS_SURCHARGE_AMT` | NUMERIC |  | The system-calculated surcharge amount. |
| 5 | `SP_DISCOUNT_AMT` | NUMERIC |  | The estimated self-pay discount amount. |
| 6 | `SYS_SP_DISCOUNT_AMT` | NUMERIC |  | The system-calculated self-pay discount amount. |
| 7 | `FA_DISCOUNT_AMT` | NUMERIC |  | The estimated financial assistance discount amount. |
| 8 | `SYS_FA_DISCOUNT_AMT` | NUMERIC |  | The system-calculated financial assistance discount amount. |
| 9 | `SOURCE_ORDER_ID` | NUMERIC |  | This is the order this line of the estimate was created from. |
| 10 | `APPLIED_DISCR_DISCOUNT_AMT` | NUMERIC |  | The applied discretionary discount amount on the estimate. |
| 11 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 12 | `SYS_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 13 | `PX_SOURCE_C_NAME` | VARCHAR |  | Stores a category describing where procedure lines on an estimate originated from. |
| 14 | `CHG_AMOUNT_SOURCE_C_NAME` | VARCHAR |  | Source of the estimated charge amount. |
| 15 | `ALLOW_AMOUNT_SOURCE_C_NAME` | VARCHAR |  | Source of the estimated allowed amount. |
| 16 | `PX_SOURCE_PAT_ENC_CSN_ID` | NUMERIC | FK→ | This is the CSN this line of the estimate was generated from by the system. |
| 17 | `SYSTEM_NDC_ID` | VARCHAR |  | This is the default NDC medication package used for pricing a medication. |
| 18 | `SYSTEM_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 19 | `OVERRIDE_NDC_ID` | VARCHAR |  | This is the NDC medication package selected by a user used for pricing a medication. |
| 20 | `OVERRIDE_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 21 | `SOURCE_TREATMENT_PLAN_ID` | NUMERIC |  | Stores the treatment plan record from where procedure lines on an estimate were pulled from. |
| 22 | `TREATMENT_DAY_LINE` | INTEGER |  | Stores the line from related group TPL 5000 for where procedure lines on an estimate were pulled from if they were added from a Beacon treatment plan. |
| 23 | `TREATMENT_BLOCK_C_NAME` | VARCHAR | org | Stores the block category type that a procedure was in when pulled in from a Beacon treatment plan. |
| 24 | `DISC_PRIC_CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the pricing contract. |
| 25 | `APPLIED_DISC_PRIC_CONTRACT_AMT` | NUMERIC |  | Discount amount calculated from the discount pricing contract. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PX_SOURCE_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

