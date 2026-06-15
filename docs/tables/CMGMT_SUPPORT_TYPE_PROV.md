# CMGMT_SUPPORT_TYPE_PROV

> This table extracts the related multiple response Support & Services Audit Trail - Responsible User (I HSB 64143) item.

**Primary key:** `EPISODE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the episode record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical support and service type information in the episode record. Together with EPISODE_ID, this forms the foreign key to the CMGMT_SUPPORT_TYPE_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple responsible providers in the snapshot of the support and services audit trail (SI HSB 64140) associated with the support and service type from the CMGMT_SUPPORT_TYPE_HX table. |
| 4 | `SUPPORT_TYPE_RESP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

