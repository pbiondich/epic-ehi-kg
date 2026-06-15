# CL_ELG

> This table contains information on allergens.

**Primary key:** `ALLERGEN_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALLERGEN_ID` | NUMERIC | PK | The ID of the allergen record. |
| 2 | `ALLERGEN_ID_ALLERGEN_NAME` | VARCHAR |  | The name of the allergen record. |
| 3 | `ALLERGEN_NAME` | VARCHAR |  | The name of the allergen record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [ALLERGY](ALLERGY.md) | `ALLERGEN_ID` | high |

