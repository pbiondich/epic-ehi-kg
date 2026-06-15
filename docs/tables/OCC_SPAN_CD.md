# OCC_SPAN_CD

> All values associated with a claim are stored in the Claim External Value record. The OCC_SPAN_CD table holds the occurrence span codes that apply to the claim.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `OCC_SPAN_CD` | VARCHAR |  | This item holds the occurrence span codes that apply to the claim. |
| 4 | `OCC_SPAN_FROM_DT` | DATETIME |  | This item holds the beginning of the date span corresponding to the occurrence span code. |
| 5 | `OCC_SPAN_TO_DT` | DATETIME |  | This item holds the end of the date span corresponding to the occurrence span code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

