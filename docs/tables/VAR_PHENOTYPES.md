# VAR_PHENOTYPES

> The VAR_PHENOTYPES table contains the external phenotype identifier and the system that defined it.

**Primary key:** `VARIANT_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANT_ID` | NUMERIC | PK FK→ | The unique identifier for the variant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PHENOTYPE_SYSTEM_C_NAME` | VARCHAR |  | The coding system category ID for the phenotype. |
| 4 | `PHENOTYPE_CODE` | VARCHAR |  | The external phenotype code assigned by the phenotype coding system. |
| 5 | `PHENOTYPE_NAME` | VARCHAR |  | Phenotype name of phenotypes associated with the variant |
| 6 | `MODE_OF_INHERITANCE_C_NAME` | VARCHAR |  | The mode of inheritance category ID for the phenotype associated with the variant |
| 7 | `PHENOTYPE_SPEC_PENETRANCE` | NUMERIC |  | The penetrance of a particular phenotype |
| 8 | `PHENOTYPE_SPEC_DESC` | VARCHAR |  | A free-text description of a particular phenotype |
| 9 | `PHENOTYPE_SPEC_VAR_CLASS_C_NAME` | VARCHAR |  | The category ID corresponding to the variant classification of a phenotype. |
| 10 | `PHENOTYPE_EFFECT_TYPE_C_NAME` | VARCHAR |  | Stores the phenotypic effect type of a variant. |
| 11 | `PHENOTYPE_EFFECT_VAL_C_NAME` | VARCHAR |  | Stores the phenotypic effect value of a variant. |
| 12 | `PHENOTYPE_ACTIVITY_SCORE_LOWER` | NUMERIC |  | The activity score of the pharmacogenomic variant, or the lowest value the activity score can be based on lab input |
| 13 | `PHENOTYPE_ACTIVITY_SCORE_UPPER` | NUMERIC |  | The highest value the activity score can be based on lab input |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VARIANT_ID` | [VARIANT](VARIANT.md) | sole_pk | high |

