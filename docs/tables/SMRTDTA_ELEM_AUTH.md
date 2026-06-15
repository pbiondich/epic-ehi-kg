# SMRTDTA_ELEM_AUTH

> This table is a bridge between authorization context SmartData element values and the source authorization records.

**Primary key:** `HLV_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the value record. |
| 2 | `AUTH_ID` | NUMERIC | FK→ | The unique ID of the linked authorization record that is associated with the SmartData element value. |
| 3 | `ELEMENT_ID` | VARCHAR | FK→ | The SmartData identifier (SDI) for this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_ID` | [AUTHORIZATIONS](AUTHORIZATIONS.md) | overflow_master | medium |
| `ELEMENT_ID` | [OR_PNDS](OR_PNDS.md) | sole_pk | high |

