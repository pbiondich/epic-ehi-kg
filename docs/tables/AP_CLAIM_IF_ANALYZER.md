# AP_CLAIM_IF_ANALYZER

> The AP_CLAIM_IF_ANALYZER table contains claim-level response data from the code editor interface that was received about a claim when run against an analyzer interface.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `START_VISIT_LEVEL` | VARCHAR |  | Visit level submitted on the claim to be processed by the analyzer interface |
| 4 | `END_VISIT_LEVEL` | VARCHAR |  | Final visit level after the analyzer makes any adjustments. |
| 5 | `START_HCPCS` | VARCHAR |  | Procedure code submitted on the claim to be processed by the analyzer. |
| 6 | `END_HCPCS` | VARCHAR |  | Final procedure code after the analyzer makes any adjustments. |
| 7 | `FINAL_PSCA` | VARCHAR |  | The final PSCA (Proportional Standard Cost Allocation) assigned to this claim taking into consideration all the reason for visit diagnosis codes, age, and gender of the patient. |
| 8 | `VISIT_REASON_PSCA` | VARCHAR |  | The PSCA (Proportional Standard Cost Allocation) assigned to each reason for visit code taking into consideration the age and gender of the patient. |
| 9 | `DIAGNOSTIC_CATEGORY` | VARCHAR |  | An array of the diagnostic test categories on the claim found by the analyzer. |
| 10 | `PSCA_WEIGHT` | VARCHAR |  | The final PSCA (Proportional Standard Cost Allocation) weight for this claim, based on all of the reason for visit diagnosis codes, as well as the patient's age and sex. |
| 11 | `DIAGNOSTIC_CATEGORY_WEIGHT` | VARCHAR |  | The weight for each diagnostic category found on this claim, based on all line-level procedure codes representing the ancillary services ordered for the patient. |
| 12 | `COMPLEXITY_WEIGHT` | VARCHAR |  | The final patient complexity weight for this claim, based on the principal diagnosis, all secondary diagnosis codes, and all external cause of injury diagnosis codes. |
| 13 | `TOTAL_WEIGHT` | VARCHAR |  | The total weight used to assign the final visit level. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

