# SERVICE_PLAN_HX_REVISION

> The SERVICE_PLAN_HX_REVISION table contains the user and instant that a service plan was modified. Information about specific items modified during the revision can be found in SERVICE_PLAN_HX_CHANGE.

**Primary key:** `SERVICE_PLAN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERVICE_PLAN_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the service plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_TRAIL_USER_ID` | VARCHAR |  | The user responsible for this revision |
| 4 | `AUDIT_TRAIL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `AUDIT_TRAIL_INSTANT_DTTM` | DATETIME (UTC) |  | The instant at which this revision was filed |
| 6 | `AUDIT_TRL_SERVICE_PLAN_CSN_ID` | NUMERIC |  | The version of the service plan for which this revision was made. Stores the CSN of the service plan version. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SERVICE_PLAN_ID` | [SERVICE_PLAN](SERVICE_PLAN.md) | sole_pk | high |

