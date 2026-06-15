# IRF_PREADMIT_INFO

> Data for the inpatient rehab facility (IRF) preadmission, including data from the IGC Spotter section.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `IMPAIRMENT_GROUP_CODE_C` | VARCHAR |  | The code that best describes the primary reason for admission to the rehab facility. |
| 3 | `ESTIMATED_MOTOR_NUM` | NUMERIC |  | The estimated motor score entered into the preadmission screening. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

