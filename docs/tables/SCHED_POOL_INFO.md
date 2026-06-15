# SCHED_POOL_INFO

> This table contains information about a scheduling pool.

**Primary key:** `POOL_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `POOL_ID` | VARCHAR | PK shared | The unique ID number of the scheduling pool used when searching for available providers for an appointment. |
| 2 | `POOL_ID_POOL_NAME` | VARCHAR |  | The name of the scheduling pool used when searching for available providers for an appointment. |
| 3 | `POOL_NAME` | VARCHAR |  | The name of the scheduling pool used when searching for available providers for an appointment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

