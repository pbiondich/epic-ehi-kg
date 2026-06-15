# BAT_DB_MAIN

> Stores unique values for the batch that do not change over time.

**Primary key:** `BATCH_NUMBER_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BATCH_NUMBER_ID` | VARCHAR | PK | The unique ID of the batch. |
| 2 | `BATCH_COMMENT_ID` | VARCHAR |  | The unique ID for the comment on the batch. |
| 3 | `INTENDED_PAT_ID` | VARCHAR | FK→ | The patient that the contents of the batch is intended for. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTENDED_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [BAT_REL_GRP](BAT_REL_GRP.md) | `BATCH_NUMBER_ID` | high |
| [BAT_REQ_IN_BATCH](BAT_REQ_IN_BATCH.md) | `BATCH_NUMBER_ID` | high |

