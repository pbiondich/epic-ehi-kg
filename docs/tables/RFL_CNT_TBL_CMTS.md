# RFL_CNT_TBL_CMTS

> Related multi table for the Counts Table - Comment (I RFL 513) item. Each line in the related multi item represents a line of text.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated external appointment in the referral record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple lines of comment text associated with an external appointment in the referral record. |
| 4 | `EXT_SVC_COMMENT` | VARCHAR |  | The comment text associated with the line number of one of the multiple lines of comment text associated with an external appointment in the referral record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

