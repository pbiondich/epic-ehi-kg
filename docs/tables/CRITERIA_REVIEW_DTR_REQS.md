# CRITERIA_REVIEW_DTR_REQS

> The DTR requests associated with the guideline review.

**Primary key:** `CRITERIA_REVIEW_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CRITERIA_REVIEW_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the review record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DTR_AUTH_ID` | NUMERIC |  | The DTR request associated with the guideline review. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CRITERIA_REVIEW_ID` | [CRITERIA_REVIEW](CRITERIA_REVIEW.md) | sole_pk | high |

