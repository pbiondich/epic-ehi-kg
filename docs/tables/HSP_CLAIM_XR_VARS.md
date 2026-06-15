# HSP_CLAIM_XR_VARS

> This table contains the values used by contract pricing extensions for calculating expected reimbursement.

**Primary key:** `CLAIM_PRINT_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the claim print record. |
| 2 | `COST_OUT_PMT_TOTAL` | NUMERIC |  | This column stores the outlier payment amount for the claim for use in claims printing. This is used for inpatient claims sent to the Health Authority of Abu Dhabi that are paid by diagnosis-related group (DRG). |
| 3 | `COST_OUT_PMT_CAND` | NUMERIC |  | The cost outlier payment total for a claim that does not include a cost outlier in its expected reimbursement amount calculation but that may be a candidate for a cost outlier. |
| 4 | `IMPLANT_PMT_TOTAL` | NUMERIC |  | This item tracks the expected reimbursement for implants. This data must be stored using a contracts pricing programming point that specifically updates this item. |
| 5 | `PHY_TRANS_PMT_TOTAL` | NUMERIC |  | The expected reimbursement for physician transplant. |
| 6 | `COST_OUT_TAX_TOTAL` | NUMERIC |  | For inpatient claims sent to the Health Authority of Abu Dhabi that are paid by DRG, this item will hold the VAT amount calculated for the Cost Outlier Payment Total for use in claims printing. This item can be used in other, mutually exclusive scenarios for expected reimbursement calculations. |
| 7 | `ADD_ON_TAX_TOTAL` | NUMERIC |  | For inpatient claims sent to the Health Authority of Abu Dhabi that are paid by DRG, this item will hold the add-on VAT amount for the claim for use in claims printing. This item can be used in other, mutually exclusive scenarios for expected reimbursement calculations. |
| 8 | `SUPPLY_ADD_ON_PMT_TOTAL` | NUMERIC |  | For inpatient claims sent to the Dubai Health Authority that are paid by DRG, this item will hold the high cost supply add-on payment amount for the claim for use in claims printing. This item can be used in other, mutually exclusive scenarios for expected reimbursement calculations. The value and specific purpose for this item may change based on the extension used. |
| 9 | `DRUG_ADD_ON_PMT_TOTAL` | NUMERIC |  | For inpatient claims sent to the Dubai Health Authority that are paid by DRG, this item will hold the high cost drug add-on payment amount for the claim for use in claims printing. This item can be used in other, mutually exclusive scenarios for expected reimbursement calculations. The value and specific purpose for this item may change based on the extension used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

