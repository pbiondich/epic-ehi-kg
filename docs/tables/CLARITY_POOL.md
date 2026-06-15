# CLARITY_POOL

> The CLARITY_POOL table contains summary information about the risk pools into which incoming capitation moneys are distributed, and from which capitation and/or AP claims payments are drawn.

**Primary key:** `POOL_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `POOL_ID` | NUMERIC | PK shared | The unique ID number of the risk pool record. |
| 2 | `POOL_ID_POOL_NAME` | VARCHAR |  | The name of the risk pool. |
| 3 | `POOL_NAME` | VARCHAR |  | The name of the risk pool. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

