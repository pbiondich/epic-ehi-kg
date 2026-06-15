# CL_RMT_PLB_INFO

> This table contains information about Provider Level Adjustments from the remittance file. It conveys provider level adjustment information for debit or credit transactions such as accelerated payments, cost report settlements for a fiscal year and timeliness report penalties unrelated to a specific claim or service.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record. |
| 2 | `PROV_IDENTIFIER` | VARCHAR |  | This column contains the provider identifier assigned by the payor for Provider Level Adjustments (PLB). Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier. |
| 3 | `FISCAL_PERIOD_DT` | DATETIME |  | This column contains the fiscal period date for Provider Level Adjustments (PLB). The last day of the provider’s fiscal year. |
| 4 | `PROV_ADJ_AMT` | NUMERIC |  | This column contains the adjustment amount for Provider Level Adjustments (PLB). |
| 5 | `PLB_ADJUSTMENT_IDN` | VARCHAR |  | This column contains the adjustment ID for Provider Level Adjustments (PLB). It provides the category and identifying reference information for an adjustment amount. This code is a composite data structure. The composite identifies the reason and identifying information for the adjustment amount. |
| 6 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. (Standard for this column type) |
| 7 | `PLB_BILL_SYS_C_NAME` | VARCHAR |  | Billing system of this Provider Level Adjustment (PLB) when remittance file has Professional Billing and Hospital Billing Payments. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

