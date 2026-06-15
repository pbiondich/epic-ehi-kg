# VARIANT_GENES

> This table stores gene data for variant results.

**Primary key:** `VARIANT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the variant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GENE_ID` | NUMERIC | FK→ | The unique ID of a gene associated with the variant record. |
| 4 | `GENE_ID_RECORD_SYMBOL` | VARCHAR |  | The current symbol for this gene. In cases of disagreement, the current HGNC symbol will be used. |
| 5 | `REPORTED_GENE_NAME` | VARCHAR |  | The name of the gene associated with the variant record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GENE_ID` | [GENE_IDENT](GENE_IDENT.md) | sole_pk | high |
| `VARIANT_ID` | [VARIANT](VARIANT.md) | sole_pk | high |

