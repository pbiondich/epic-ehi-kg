# ORD_CV_F_TEXT

> This table contains the text to display for a cardiovascular finding.

**Primary key:** `CV_FINDING_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CV_FINDING_ID` | NUMERIC | PK FK→ | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FINDINGS_TEXT` | VARCHAR |  | Stores textual description for this finding. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CV_FINDING_ID` | [ORD_CV_FINDING](ORD_CV_FINDING.md) | sole_pk | high |

