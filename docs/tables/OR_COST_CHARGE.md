# OR_COST_CHARGE

> The OR_COST_CHARGE table stores the general information about Cost, Charge Code and Charge Markup tables.

**Primary key:** `COST_TABLE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COST_TABLE_ID` | NUMERIC | PK | ID of the Cost/Charge Code Table. This is an unique ID for each Cost/Charge Code Table. |
| 2 | `COST_TABLE_ID_COST_TABLE_NAME` | VARCHAR |  | Name of the Cost/Charge Code Table |
| 3 | `COST_TABLE_NAME` | VARCHAR |  | Name of the Cost/Charge Code Table |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

