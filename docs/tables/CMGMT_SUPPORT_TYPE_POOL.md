# CMGMT_SUPPORT_TYPE_POOL

> This table extracts the related multiple response Support & Services Audit Trail - Responsible Pool (I HSB 64144) item.

**Primary key:** `EPISODE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the episode record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical support and service type information in the episode record. Together with EPISODE_ID, this forms the foreign key to the CMGMT_SUPPORT_TYPE_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple responsible pools in the snapshot of the support and services audit trail (SI HSB 64140) associated with the support and service type from the CMGMT_SUPPORT_TYPE_HX table. |
| 4 | `SUPPORT_TYPE_RESP_REGISTRY_ID` | NUMERIC |  | The unique identifier of the historical responsible pool for the support and service type. |
| 5 | `SUPPORT_TYPE_RESP_REGISTRY_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

