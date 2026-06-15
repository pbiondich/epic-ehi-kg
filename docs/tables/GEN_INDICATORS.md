# GEN_INDICATORS

> The GEN_INDICATORS table contains information about your genomic indicator records. These include disease-related and drug-related genomic indicators.

**Primary key:** `GEN_INDICATOR_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GEN_INDICATOR_ID` | NUMERIC | PK | This column contains the unique identifier (.1 item) for the indicator record. |
| 2 | `RESOLVED_PAT_FRIENDLY_NAME` | VARCHAR |  | This column provides an always populated name column that prioritizes the patient friendly name and if there is none specified, falls back to the clinical name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [ALERT_GENOMIC_INDICATORS](ALERT_GENOMIC_INDICATORS.md) | `GEN_INDICATOR_ID` | high |

