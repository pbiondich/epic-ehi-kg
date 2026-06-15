# HH_INTVTN_INFO

> Contains Home Health care plan intervention noadd single items information.

**Primary key:** `INTERVENTION_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | VARCHAR | PK FK→ | Unique identifier for the care plan intervention. |
| 2 | `INTRVNTION_TYPE_ID_INTRVNTN_TYPE_NAME` | VARCHAR |  | The name of the intervention type. |
| 3 | `CREATE_DATE` | DATETIME (Local) |  | Care plan intervention creation date. |
| 4 | `DELETE_DATE` | DATETIME (Local) |  | Care plan intervention deleted date. |
| 5 | `INITIAL_NOTES_ID` | VARCHAR |  | Care plan intervention initial notes ID. |
| 6 | `REQ_ORDER_UPDATE_C_NAME` | VARCHAR |  | This item tracks whether an intervention should require an order when updated. |
| 7 | `HH_EPISODE_ID` | NUMERIC |  | The associated episode ID for a care plan intervention. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

