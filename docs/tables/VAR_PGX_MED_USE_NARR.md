# VAR_PGX_MED_USE_NARR

> This table stores the medication usage narrative for a pharmacogenomic variant.

**Primary key:** `VARIANT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANT_ID` | NUMERIC | PK FK→ | The unique identifier for the variant record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the medication usage narrative for a pharmacogenomic variant. Together with VARIANT_ID, this forms the foreign key to the VAR_PGX_MED_USE_NARR table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of a portion of the medication usage narrative associated with the pharmacogenomic variant and medication from the VAR_PGX_MED_USE table |
| 4 | `MED_USE_NARRATIVE` | VARCHAR |  | Free text field denoting alteration to medication based on drug-gene interactions |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VARIANT_ID` | [VARIANT](VARIANT.md) | sole_pk | high |

