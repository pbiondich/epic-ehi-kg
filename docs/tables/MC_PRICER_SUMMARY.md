# MC_PRICER_SUMMARY

> This table contains pricing summary output returned by the Epic Pricer.

**Primary key:** `PRICER_MSG_ID`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier for the Pricer Message record. |
| 2 | `PRICE_SUM_ALLOW` | NUMERIC |  | Returned allowed amount from pricing summary data. |
| 3 | `PRICE_SUM_PMT` | NUMERIC |  | Returned payment amount from pricing summary data. This is a calculation of the allowed amount minus coinsurance/deductible. |
| 4 | `PRICE_SUM_DEDUCT` | NUMERIC |  | Returned deductible amount from pricing summary data. |
| 5 | `PRICE_SUM_COINS` | NUMERIC |  | Returned coinsurance amount from pricing summary data. |
| 6 | `PRICE_SUM_OUTLIER` | NUMERIC |  | Returned outlier amount from pricing summary data. |
| 7 | `PRICE_SUM_HCPCS_RTN_C_NAME` | VARCHAR |  | The returned HCPCS Pricer return code from pricing summary data. |
| 8 | `PRICE_SUM_FSC_AMT` | NUMERIC |  | Returned fee schedule amount from pricing summary data. |
| 9 | `IS_NON_FACILITY_RATE_YN` | VARCHAR |  | Indicator for whether the service is paid using the non-facility rate in the Medicare Physician Fee Schedule. |
| 10 | `ALLOWED_AMT_BEFORE_ADJ` | NUMERIC |  | Medicare fee schedule allowed amount before any pricing adjustments. |
| 11 | `UNITS_APPLIED` | NUMERIC |  | Number of units applied to the base fee schedule rate to determine the Medicare allowed amount. |
| 12 | `PRICE_SUM_CLAIM_DRG` | VARCHAR |  | The DRG code used by the Epic Pricer to price a claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

