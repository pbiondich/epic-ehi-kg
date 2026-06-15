# CASE_CHARGE

> The CASE_CHARGE table allows you to report on charges associated with cases in the Chronic Disease Case Management module.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The line number of the charges associated with this case record. |
| 3 | `CHARGE_ID` | NUMERIC |  | The unique ID of the charge record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

