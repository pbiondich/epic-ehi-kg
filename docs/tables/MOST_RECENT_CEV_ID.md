# MOST_RECENT_CEV_ID

> This table contains data for the most recent claim external values (CEV) records for each CEV context.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MOST_RECENT_CEV_ID` | NUMERIC |  | The most recent CEV ID for the given CEV context. |
| 4 | `CEV_CONTEXT_C_NAME` | VARCHAR |  | This column contains the Claim External Values (CEV) context (direction of claim file, incoming or outgoing) |
| 5 | `CEV_UPDATE_DTTM` | DATETIME (Local) |  | This column contains the update instant (local time zone) for the most recent Claim External Values (CEV) for the given CEV context. |
| 6 | `CEV_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | Update instant for the most recent CEV for the given CEV context. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

