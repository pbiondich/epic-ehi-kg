# CASE_ROSTER

> The CASE_ROSTER table is the master table to report on case roster information.

**Primary key:** `ROSTER_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ROSTER_ID` | VARCHAR | PK | The unique identifier for the roster record. |
| 2 | `ROSTER_ID_ROSTER_NAME` | VARCHAR |  | The name of the roster. |
| 3 | `ROSTER_NAME` | VARCHAR |  | The name of the roster. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [CASE_MGMT](CASE_MGMT.md) | `ROSTER_ID` | high |

