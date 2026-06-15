# VAR_ALLELE_NAME

> The VAR_ALLELE_NAME table contains information about the alleles the variant belongs to.

**Primary key:** `VARIANT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANT_ID` | NUMERIC | PK FK→ | The unique identifier for the variant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ALLELE_NAME` | VARCHAR |  | The allele names to which the variants belong. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VARIANT_ID` | [VARIANT](VARIANT.md) | sole_pk | high |

