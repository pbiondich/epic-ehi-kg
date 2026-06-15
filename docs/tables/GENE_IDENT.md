# GENE_IDENT

> Version-independent information about a gene record such as its name or HUGO Gene Nomenclature (HGNC) ID.

**Primary key:** `GENE_ID`  
**Columns:** 2  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GENE_ID` | NUMERIC | PK | The unique identifier (.1 item) for the gene record. |
| 2 | `RECORD_SYMBOL` | VARCHAR |  | The current symbol for this gene. In cases of disagreement, the current HGNC symbol will be used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [VARIANT](VARIANT.md) | `GENE_ID` | high |
| [VARIANT_GENES](VARIANT_GENES.md) | `GENE_ID` | high |

