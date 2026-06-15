# HSP_BKT_EOB_INFO

> This table contains claims-related explanation of benefits (EOB) information for liability buckets.

**Primary key:** `BUCKET_ID`, `LINE`  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | This column stores the unique identifier for the bucket record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EOB_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 4 | `EOB_PMT_HTR_ID` | NUMERIC |  | This column stores the payment transaction record for the claim explanation of benefits (EOB) information associated with this liability bucket. |
| 5 | `EOB_ORIG_BKT_ID` | NUMERIC |  | The original liability bucket record for the claim EOB information associated with this liability bucket. |
| 6 | `EOB_CVG_ID` | NUMERIC |  | The coverage record for the claim EOB information associated with this liability bucket. |
| 7 | `EOB_INV_NUM` | VARCHAR |  | The invoice number for the claim EOB information associated with this liability bucket. |
| 8 | `EOB_DEPOSIT_DATE` | DATETIME |  | The deposit date for the claim EOB information associated with this liability bucket. |
| 9 | `EOB_PMT_AMT` | NUMERIC |  | The payment amount for the claim EOB information associated with this liability bucket. |
| 10 | `EOB_ICN` | VARCHAR |  | This column stores the internal control number information for the claim EOB information associated with this liability bucket. |
| 11 | `EOB_ALLOW_AMT` | NUMERIC |  | The allowed amount for the claim EOB information associated with this liability bucket. |
| 12 | `EOB_NOT_ALLOW_AMT` | NUMERIC |  | The not allowed amount for the claim EOB information associated with this liability bucket. |
| 13 | `EOB_DEDUCT_AMT` | NUMERIC |  | The deductible amount for the claim EOB information associated with this liability bucket. |
| 14 | `EOB_COINS_AMT` | NUMERIC |  | The coinsurance amount for the claim EOB information associated with this liability bucket. |
| 15 | `EOB_COPAY_AMT` | NUMERIC |  | The copay amount for the claim EOB information associated with this liability bucket. |
| 16 | `EOB_COB_AMT` | NUMERIC |  | This column stores the coordination of benefits amount for the claim EOB information associated with this liability bucket. |
| 17 | `EOB_ADJ_AMT` | NUMERIC |  | The adjustment amount for the claim EOB information associated with this liability bucket. |
| 18 | `EOB_NON_COVERED_AMT` | NUMERIC |  | The non covered amount for the claim EOB information associated with this liability bucket. |
| 19 | `EOB_IMD_ID` | VARCHAR |  | This column stores the remittance image record (IMD) for the claim EOB information associated with this liability bucket. |
| 20 | `EOB_POST_DATE` | DATETIME |  | The post date for the claim EOB information associated with this liability bucket. |
| 21 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | Hospital account record associated with this liability bucket. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

