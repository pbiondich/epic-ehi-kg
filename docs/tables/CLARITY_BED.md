# CLARITY_BED

> This table reflects the data in the Hospital Beds (BED) master file.

**Primary key:** `BED_CSN_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BED_CSN_ID` | NUMERIC | PK | The serial number for the bed contact of the bed record. This number is unique across all bed contacts in the system. |
| 2 | `BED_LABEL` | VARCHAR |  | The name of the bed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [CLARITY_ADT](CLARITY_ADT.md) | `BED_CSN_ID` | high |

