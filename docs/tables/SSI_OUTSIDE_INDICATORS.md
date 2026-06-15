# SSI_OUTSIDE_INDICATORS

> This table contains Infection Control surgical site infection surveillance data that tracks readmissions, diagnoses, post-prophylaxis antibiotics, and lab results from outside sources through the surveillance period.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the abstraction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OUTSIDE_IND_TYPE_C_NAME` | VARCHAR |  | The category number for the outside SSI indicator type found by the SSI Surveillance batch job. |
| 4 | `OUTSIDE_IND_VALUE` | VARCHAR |  | The outside data value for indicators found by the SSI Surveillance batch job. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

