# SMRTDTA_ELEM_AIEXTRACTED

> This table is a bridge between AI Extracted Fact context SmartData element values and the source interaction records.

**Primary key:** `HLV_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the value record. |
| 2 | `ELEMENT_ID` | VARCHAR | FK→ | The SmartData identifier (SDI). |
| 3 | `AI_INTRCT_ID` | NUMERIC | FK→ | Record ID of the context contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AI_INTRCT_ID` | [AI_INTRCT_INFO](AI_INTRCT_INFO.md) | sole_pk | high |
| `ELEMENT_ID` | [OR_PNDS](OR_PNDS.md) | sole_pk | high |

