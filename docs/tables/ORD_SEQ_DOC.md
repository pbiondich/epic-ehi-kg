# ORD_SEQ_DOC

> This table contains order-level information associated with genomics sequencing documents.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SEQ_DOC_ID` | NUMERIC | FK→ | The unique identifier for the genomics sequencing pipeline document (PDS) associated with the order. |
| 4 | `ORD_SEQ_DOC_SAMPLE_TYP_C_NAME` | VARCHAR |  | The sample type category ID for the associated genomics sequencing document. Sample type represents the relationship between the patient on the order and the source of the genomic sample from which the sequencing document was generated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SEQ_DOC_ID` | [SEQ_DOC](SEQ_DOC.md) | sole_pk | high |

