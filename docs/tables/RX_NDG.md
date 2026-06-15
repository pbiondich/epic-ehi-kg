# RX_NDG

> This table can be used to extract data related with package information, associated medication, implied unit, physical owner, and logical owner for National Drug Code (NDC) grouper records.

**Primary key:** `NDG_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NDG_ID` | NUMERIC | PK | The unique ID for the NDG (NDC Grouper). |
| 2 | `NDG_ID_NDG_NAME` | VARCHAR |  | Name of the NDC Grouper record. |
| 3 | `NDG_NAME` | VARCHAR |  | Name of the NDC Grouper record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

