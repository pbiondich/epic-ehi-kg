# OCC_CD

> All values associated with a claim are stored in the Claim External Value record. The OCC_CD table holds the occurrence codes that apply to the claim.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `OCC_CD` | VARCHAR |  | This item holds the occurrence codes that apply to the claim. |
| 4 | `OCC_DT` | DATETIME |  | This item holds the date corresponding to the occurrence code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

