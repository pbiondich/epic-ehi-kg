# PATTERNS

> The PATTERNS table contains information about stored Patterns that can be used to create schedule templates for providers.

**Primary key:** `PATTERN_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PATTERN_ID` | VARCHAR | PK shared | The unique ID number of the pattern record used to create a provider's schedule. |
| 2 | `PATTERN_ID_PATTERN_NAME` | VARCHAR |  | The name of the pattern record used to create a provider's schedule. |
| 3 | `PATTERN_NAME` | VARCHAR |  | The name of the pattern record used to create a provider's schedule. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

