# PB_FORMAT

> The PB_FORMAT table contains the premium billing invoice formats.

**Primary key:** `PB_FORMAT_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_FORMAT_ID` | VARCHAR | PK | The unique ID of the premium billing invoice format. |
| 2 | `FORMAT_NAME` | VARCHAR |  | Name of the premium billing invoice format |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [PB_ACCT](PB_ACCT.md) | `PB_FORMAT_ID` | high |

