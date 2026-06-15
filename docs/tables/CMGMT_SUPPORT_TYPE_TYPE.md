# CMGMT_SUPPORT_TYPE_TYPE

> This table extracts the related multiple response Support & Services Audit Trail - Type (I HSB 64140) item.

**Primary key:** `EPISODE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the episode record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical support and service type information in the episode record. Together with EPISODE_ID, this forms the foreign key for CMGMT_SUPPORT_TYPE_HX. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of the support and services type in the snapshot of the support and services audit trail (SI HSB 64140) and associated with the support and service type in CMGMT_SUPPORT_TYPE_HX. |
| 4 | `SC_SUPPORT_TYPE_C_NAME` | VARCHAR | org | The support and service type category ID for the episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

