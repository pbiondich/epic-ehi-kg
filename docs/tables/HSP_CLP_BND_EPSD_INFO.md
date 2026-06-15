# HSP_CLP_BND_EPSD_INFO

> Holds rows for every claim line / linked bundled episode combination on a claim.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the claim print record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BND_EPSD_EPISODE_ID` | NUMERIC |  | Holds the bundled episode record that is linked to the related claim line. |
| 4 | `BND_EPSD_CLAIM_LINE` | INTEGER |  | Holds the claim line that is linked to the related bundled episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

