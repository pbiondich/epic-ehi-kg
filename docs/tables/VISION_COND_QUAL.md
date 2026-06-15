# VISION_COND_QUAL

> This table holds vision condition qualifiers.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `VISION_COND_QUAL` | VARCHAR |  | This item identifies the reason for the vision services when the claim contains charges for replacement frames or lenses. |
| 4 | `VISION_COND_CD_YN` | VARCHAR |  | Indicates whether the condition code is related to vision services. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

