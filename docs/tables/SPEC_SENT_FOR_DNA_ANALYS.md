# SPEC_SENT_FOR_DNA_ANALYS

> This table stores whether the specimen was sent to a geneticist for chromosome analysis.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SENT_FOR_CHROM_ANALYSIS_C_NAME` | VARCHAR | org | The category ID for whether the specimen was sent to a geneticist for chromosome analysis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

