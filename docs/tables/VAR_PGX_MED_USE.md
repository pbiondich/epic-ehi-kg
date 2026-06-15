# VAR_PGX_MED_USE

> Drug-specific information related to a pharmacogenomic variant.

**Primary key:** `VARIANT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANT_ID` | NUMERIC | PK FK→ | The unique identifier for the variant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PGX_MED_CODESET_C_NAME` | VARCHAR |  | The medication coding system category for the pharmacogenomic variant. |
| 4 | `PGX_MED_CODE` | VARCHAR |  | Code for the medication being assessed for usage suggestions based on drug-gene interactions. |
| 5 | `ASSOC_MED_NAME` | VARCHAR |  | Name of the medication being assessed for usage suggestions based on drug-gene interactions. |
| 6 | `MED_USE_CATEGORY_C_NAME` | VARCHAR |  | The medication usage suggestion category for the pharmacogenomic variant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VARIANT_ID` | [VARIANT](VARIANT.md) | sole_pk | high |

