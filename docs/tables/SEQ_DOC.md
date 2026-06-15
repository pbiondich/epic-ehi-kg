# SEQ_DOC

> This table contains information about your genomics sequencing pipeline documents.

**Primary key:** `SEQ_DOC_ID`  
**Columns:** 5  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SEQ_DOC_ID` | NUMERIC | PK | The unique identifier for the sequencing document record. |
| 2 | `CLOUD_VOL_AND_BLOB` | VARCHAR |  | The cloud volume and blob name where the sequencing document is stored |
| 3 | `PAT_ID` | VARCHAR | FK→ | The primary patient for this sample. Only sample types of Tumor and ProbandGL are considered for this association. |
| 4 | `SEQ_DOC_FILE_CLASS_C_NAME` | VARCHAR |  | The file class category ID for the sequencing document. |
| 5 | `FILE_DESC` | VARCHAR |  | This item holds a user facing description of the sequencing document. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [ORD_SEQ_DOC](ORD_SEQ_DOC.md) | `SEQ_DOC_ID` | high |
| [SEQ_DOC_COLUMN_INFO](SEQ_DOC_COLUMN_INFO.md) | `SEQ_DOC_ID` | high |

