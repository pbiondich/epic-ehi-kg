# HSP_CLP_BND_EPSD_CREATE

> This table extracts the list of episodes that this claim created.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the claim print record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CREATED_EPISODE_ID` | NUMERIC |  | The list of episodes this claim created. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

