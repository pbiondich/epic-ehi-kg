# ORDER_RAD_RVSN_RSN

> ORDER_RAD_RVSN_RSN stores the comment associated with an order marked as "needs revision" in the imaging applications. Orders are generally marked as "needs revision" by the transcriptionist when he or she needs additional information or clarification from the physician.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of lines in the revision reason comment for an order. |
| 3 | `REVISION_CMT` | VARCHAR |  | A free text comment entered by a transcriptionist to explain why clarification is needed for a reading physician's dictation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

