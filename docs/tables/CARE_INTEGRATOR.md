# CARE_INTEGRATOR

> This table contains the contact information for a Care Integrator record.

**Primary key:** `CARE_INTG_ID`, `CONTACT_DATE_REAL`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CARE_INTG_ID` | VARCHAR | PK FK→ | The unique ID for the care integrator record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The DTE contact date for the care integrator record. |
| 3 | `CAREPLAN_DISPLAY_NAME` | VARCHAR |  | The display name of the care plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CARE_INTG_ID` | [CAREPLAN_INFO](CAREPLAN_INFO.md) | sole_pk | high |

