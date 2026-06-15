# CL_COST_CNTR

> The CL_COST_CNTR table contains billing cost center information.

**Primary key:** `COST_CNTR_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COST_CNTR_ID` | NUMERIC | PK | This column stores the unique identifier for the cost center or rate center record. |
| 2 | `COST_CNTR_ID_COST_CENTER_NAME` | VARCHAR |  | The name of the cost center. |
| 3 | `COST_CENTER_NAME` | VARCHAR |  | The name of the cost center. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

