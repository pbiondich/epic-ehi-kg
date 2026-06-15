# SUPPLY_LOT

> This table stores information for supply-type Lot Number (LOT) records.

**Primary key:** `LOT_NUM_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOT_NUM_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the lot number record. |
| 2 | `LOT_NUM_NM` | VARCHAR |  | Stores the LOT number/name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

