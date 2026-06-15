# PAT_PHENO_BASIC_INFO

> This table contains basic information about a patient's phenotypes.

**Primary key:** `PAT_PHENO_ID`  
**Columns:** 4  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_PHENO_ID` | NUMERIC | PK | The unique identifier for the phenotype record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The patient associated with the patient phenotype. |
| 3 | `RECORD_CREATION_DATE` | DATETIME |  | Stores the date the record was created |
| 4 | `CURR_CONTACT_DATE_REAL` | FLOAT |  | The date when the phenotype was last updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [PAT_PHENO](PAT_PHENO.md) | `PAT_PHENO_ID` | high |

