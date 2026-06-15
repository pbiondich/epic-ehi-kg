# COMP_ASMT_REVIEW

> The COMP_ASMT_REVIEW table contains information about which users marked the hospice comprehensive assessment as reviewed and when.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CA_REVIEW_USER_ID` | VARCHAR |  | Holds the user record ID of the user who marked the comprehensive assessment as reviewed. |
| 4 | `CA_REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CA_REVIEW_DTTM` | DATETIME (UTC) |  | Stores the UTC instant at which the comprehensive assessment was marked as reviewed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

