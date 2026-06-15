# CONCEPT_COMMENT

> The CONCEPT_COMMENT table records the comments entered via SmartForms.

**Primary key:** `HLV_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique ID of the concept value record. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `CURRENT_COMMENT` | VARCHAR |  | Stores the current comment associated with a specific value. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

