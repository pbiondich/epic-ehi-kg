# LOCALE

> This table contains information about locales and the geographic pricing cost index.

**Primary key:** `LOCALE_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOCALE_ID` | NUMERIC | PK | The unique identifier for the locale record. |
| 2 | `LOCALE_ID_LOCALE_NAME` | VARCHAR |  | The name of the locale record. |
| 3 | `LOCALE_NAME` | VARCHAR |  | The name of the locale record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [PPS_INFO](PPS_INFO.md) | `LOCALE_ID` | high |

