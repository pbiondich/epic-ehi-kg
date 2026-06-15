# CL_MYC_MED

> This table contains high-level information for medications. It is similar to CLARITY_MEDICATION, but it is used exclusively by web based chart system. When a web based chart system patient enters a medication name in medication section of Your Health Record, this table will be searched for a matching medication.

**Primary key:** `MYC_MED_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MYC_MED_ID` | VARCHAR | PK | The unique ID assigned to the web based chart system medication record |
| 2 | `MYC_MED_ID_MED_NAME` | VARCHAR |  | The name of the web based chart system medication. |
| 3 | `MED_NAME` | VARCHAR |  | The name of the web based chart system medication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

