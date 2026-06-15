# PAT_ENC_WT_LST

> This table contains data related to the Wait List contact type. Each record is based on patient contact serial number.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across patients and encounters in your system. |
| 2 | `WT_LST_TKT_ID` | NUMERIC | discont. | The unique ID of the scheduling ticket which is linked to this wait list entry. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

