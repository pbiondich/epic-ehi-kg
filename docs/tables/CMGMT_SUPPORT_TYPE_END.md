# CMGMT_SUPPORT_TYPE_END

> This table extracts the related multiple response Support & Services Provided Audit Trail - End Date (I HSB 64142) item.

**Primary key:** `EPISODE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the episode record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical support and service type information in the episode record. Together with EPISODE_ID, this forms the foreign key for CMGMT_SUPPORT_TYPE_HX. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of the end date in the snapshot of the support and services audit trail (SI HSB 64140) and associated with the support and service type in CMGMT_SUPPORT_TYPE_HX. |
| 4 | `SSP_END_DATE` | DATETIME |  | The end date of historical support and service type information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

