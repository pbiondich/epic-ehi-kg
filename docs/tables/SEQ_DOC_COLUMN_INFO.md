# SEQ_DOC_COLUMN_INFO

> Stores the sample column information for sequencing documents.

**Primary key:** `SEQ_DOC_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SEQ_DOC_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the sequencing document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COLUMN_NAME` | VARCHAR |  | Stores the name of the sample column from the header line of the associated VCF File. |
| 4 | `ORD_SEQ_DOC_SAMPLE_TYP_C_NAME` | VARCHAR |  | Stores the sample type for the sample column from the header line of the assocaited VCF File. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SEQ_DOC_ID` | [SEQ_DOC](SEQ_DOC.md) | sole_pk | high |

