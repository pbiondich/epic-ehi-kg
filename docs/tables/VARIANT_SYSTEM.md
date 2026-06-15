# VARIANT_SYSTEM

> The VARIANT_SYSTEM table contains the external variant identifier and the system that defined it and its version.

**Primary key:** `VARIANT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANT_ID` | NUMERIC | PK FK→ | The unique identifier for the variant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VARIANT_SYSTEM_C_NAME` | VARCHAR |  | The source system category ID for the external variant identifier. |
| 4 | `VARIANT_SYSTEM_VER` | VARCHAR |  | The version of the external source that defined the external variant identifier. |
| 5 | `VARIANT_CODE` | VARCHAR |  | The external variant identifier assigned by the variant source. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VARIANT_ID` | [VARIANT](VARIANT.md) | sole_pk | high |

