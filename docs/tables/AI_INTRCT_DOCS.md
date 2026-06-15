# AI_INTRCT_DOCS

> Tracks documents associated with the workflow.

**Primary key:** `AI_INTRCT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AI_INTRCT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the interaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DOCUMENT_ID` | NUMERIC | shared | Pointer to the documents associated with the workflow. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AI_INTRCT_ID` | [AI_INTRCT_INFO](AI_INTRCT_INFO.md) | sole_pk | high |

