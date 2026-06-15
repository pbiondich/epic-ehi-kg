# CVG_PREMIUM_RATES

> Coverage level premium rates.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PREMIUM_RATE_EFF_DT` | DATETIME |  | Stores the effective date of the coverage level premium rate. |
| 4 | `PREMIUM_RATE` | NUMERIC |  | Stores the coverage level override premium rate. |
| 5 | `PREMIUM_RT_TERM_DT` | DATETIME |  | Stores the term date of the coverage level premium rate |
| 6 | `HIX_APTC_AMT` | NUMERIC |  | Stores the Advance Premium Tax Credit amount. |
| 7 | `HIX_CSR_AMT` | NUMERIC |  | Stores the Cost Sharing Reduction amount of an exchange coverage. |
| 8 | `HIX_OTHER_AMT` | NUMERIC |  | The payment amount for an exchange coverage from a federally recognized tribe. |
| 9 | `HIX_EMPLOYER_AMT` | NUMERIC |  | Stores the employer responsibility amount for an exchange coverage. |
| 10 | `HIX_RESP_AMT` | NUMERIC |  | Stores the total responsibility amount for an exchange coverage. |
| 11 | `HIX_STATE_AMOUNT` | NUMERIC |  | The payment amount for an exchange coverage from the state |
| 12 | `MCARE_PART_C_PREM` | NUMERIC |  | This column stores the amount for the Part C premium, which is used for Medicare Advantage coverages. |
| 13 | `MCARE_PART_D_PREM` | NUMERIC |  | This column stores the amount for the Part D premium. This value is compared to the Part D premium amount on the employer group during premium computation. This value isn't directly used for billing. The adjusted Part D premium (CVG-18838), which is used for billing, is calculated using this amount. |
| 14 | `MCARE_LATE_ENRL_PEN` | NUMERIC |  | This column holds the amount for Part D Late Enrollment Penalty (LEP), which is used for some Medicare Advantage coverages. |
| 15 | `MCARE_LIS_PART_D` | NUMERIC |  | This column holds the Low Income Subsidy (LIS) amount for Part D on Medicare Advantage coverages. |
| 16 | `MCARE_LIS_FOR_LEP` | NUMERIC |  | This column holds the Low Income Subsidy (LIS) for Late Enrollment Penalty (LEP); this is only used for Medicare Advantage coverages. |
| 17 | `MCARE_LEP_WAIVED` | NUMERIC |  | This column holds the amount of waived Late Enrollment Penalty (LEP) for Medicare Advantage coverages. |
| 18 | `MCARE_ADJ_LEP` | NUMERIC |  | This column holds the adjusted Late Enrollment Penalty. The Low Income Subsidy for Late Enrollment Penalty (CVG-18835) and the Late Enrollment Penalty Waived (CVG-18836) are each subtracted from the Late Enrollment Penalty (CVG-18833) to arrive at this amount. This amount will then be billed to the member. |
| 19 | `MCARE_ADJ_PART_D` | NUMERIC |  | This column holds the adjusted Part D premium. The Low Income Subsidy for Part D (CVG-18834) is subtracted from the Part D premium (CVG-18832) to arrive at this amount. |
| 20 | `HIX_NON_HYDE_AMOUNT` | NUMERIC |  | The non-Hyde credit amount for an exchange coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

