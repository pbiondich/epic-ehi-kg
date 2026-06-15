# V_EHI_ORD_LINKED_RQGS

> Placeholder view for ORD EHI data that needs to be marked as both static and dynamic.

**Primary key:** `ORDER_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the procedure order record. |
| 2 | `GROUPER_ID` | NUMERIC | FK→ | The unique ID of patient and coverage information for non-participatory lab referrals attached to this order. If this is filled in, then PAT_ID and related columns in the ORDER_PROC table will not be filled in for this order. This column is frequently used to link to the RQG_DB_MAIN table. |
| 3 | `CM_LOG_OWNER_ID` | VARCHAR |  | ID of the logical deployment owner for this record. Logical owners show the deployment where the record was created but doesn't represent if the record is a part of version skew. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GROUPER_ID` | [SCHEDULING_GROUPER_INFO](SCHEDULING_GROUPER_INFO.md) | sole_pk | high |

