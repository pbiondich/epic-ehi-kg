# BENEFITS_TEMPLATE

> This table contains templates for building health plan benefits.

**Primary key:** `BEN_TEMPLT_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BEN_TEMPLT_ID` | NUMERIC | PK | The unique identifier for the benefits template record. |
| 2 | `TEMPLATE_NAME` | VARCHAR |  | The name of the benefits template record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [AP_CLAIM_PROC_4](AP_CLAIM_PROC_4.md) | `BEN_TEMPLT_ID` | high |

