# ORTHO_CHG_PLAN_COVERAGES

> This table contains coverages for orthodontic charging plans.

**Primary key:** `DENTAL_BILLING_PLAN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DENTAL_BILLING_PLAN_ID` | VARCHAR | PK | The unique identifier for the treatment plan record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `ORTHODONTIC_COVERAGE_ID` | NUMERIC |  | The unique coverage ID for the orthodontic charging plan line. This is only set for insurance plans and should be used if a payer (I DTP 404) isn't specified. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

