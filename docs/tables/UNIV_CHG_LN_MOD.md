# UNIV_CHG_LN_MOD

> This table contains modifier information for charges in the Universal Charge Line (UCL) master file.

**Primary key:** `UCL_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK FK→ | The unique ID assigned to the charge line record. |
| 2 | `LINE` | INTEGER | PK | Each Universal Charge Line can have multiple modifiers associated with it. The combination of UCL_ID and LINE make up a unique identifier for this modifier. |
| 3 | `MODIFIER_ID` | VARCHAR | FK→ | The modifier associated with the Universal Charge Line. |
| 4 | `MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MODIFIER_ID` | [CLARITY_MOD](CLARITY_MOD.md) | sole_pk | high |
| `UCL_ID` | [CLARITY_UCL](CLARITY_UCL.md) | sole_pk | high |

