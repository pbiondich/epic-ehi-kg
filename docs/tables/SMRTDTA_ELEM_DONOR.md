# SMRTDTA_ELEM_DONOR

> This table is a bridge between donor context SmartData element values and the source donor records.

**Primary key:** `HLV_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the value record. |
| 2 | `DONOR_RECORD_ID` | NUMERIC |  | The unique ID of the linked donor record that is associated with the SmartData element value. |
| 3 | `ELEMENT_ID` | VARCHAR | FK→ | The SmartData identifier (SDI). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ELEMENT_ID` | [OR_PNDS](OR_PNDS.md) | sole_pk | high |

