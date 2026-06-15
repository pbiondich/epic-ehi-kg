# RYN_WHT_MED_INSURANCE

> Ryan White table for patient's medical insurance status.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RYN_WHT_MED_INSURANCE_C_NAME` | VARCHAR |  | The patient's current medical insurance. |
| 4 | `RYN_WHT_INSURANCE_OTHER` | VARCHAR |  | If the patient's Ryan White reporting insurance is Other, this item specifies what the other insurance is. |
| 5 | `RYN_WHT_INSURANCE_DATE` | DATETIME |  | The start date corresponding to the patient's Ryan White insurance. |
| 6 | `RYN_WHT_INSURANCE_FULL_LIS_YN` | VARCHAR |  | Indicates whether the patient's insurance is a Low-Income Subsidy for Ryan White reporting. |
| 7 | `RW_INSURANCE_HIGH_RISK_POOL_YN` | VARCHAR |  | Indicates whether the patient's insurance is a High-Risk Pool for Ryan White reporting. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

