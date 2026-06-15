# SRS_INFO

> Table that holds information about the questionnaire series (LQW) that does not change with time like series type, series name..etc.

**Primary key:** `SERIES_ID`  
**Columns:** 2  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERIES_ID` | NUMERIC | PK | The unique identifier (.1 item) for the qnr series record. |
| 2 | `SERIES_NAME` | VARCHAR |  | The name for the questionnaire series record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [ENROLL_QUESR_SERIES](ENROLL_QUESR_SERIES.md) | `SERIES_ID` | high |
| [SRS_ASGN_INFO](SRS_ASGN_INFO.md) | `SERIES_ID` | high |

