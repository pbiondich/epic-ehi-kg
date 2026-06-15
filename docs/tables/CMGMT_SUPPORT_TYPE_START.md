# CMGMT_SUPPORT_TYPE_START

> This table extracts the related multiple response Support & Services Audit Trail - Start Date (I HSB 64141) item.

**Primary key:** `EPISODE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the episode record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical support and service type information in the episode. Together with EPISODE_ID, the forms the foreign key to the CMGMT_SUPPORT_TYPE_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of the start date in the snapshot of the support and services audit trail (SI HSB 64140) and associated with the support and service type in CMGMT_SUPPORT_TYPE_HX. |
| 4 | `SSP_START_DATE` | DATETIME |  | The start date of historical support and service type information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

