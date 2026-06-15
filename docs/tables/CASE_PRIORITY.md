# CASE_PRIORITY

> The CASE_PRIORITY table contains information about case priority (NMP) records.

**Primary key:** `PRIORITY_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRIORITY_ID` | NUMERIC | PK | The unique identifier for the priority record. |
| 2 | `PRIORITY_ID_PRIORITY_NAME` | VARCHAR |  | The name of the priority record. |
| 3 | `PRIORITY_NAME` | VARCHAR |  | The name of the priority record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [CASE_MGMT](CASE_MGMT.md) | `PRIORITY_ID` | high |

