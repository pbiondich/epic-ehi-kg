# SERVICE_PLAN_HX_CHANGE

> The SERVICE_PLAN_HX_CHANGE table contains details of what items were modified in a revision of a service plan. Information about the user modifying the service plan and the time of modification can be found in SERVICE_PLAN_HX_REVISION.

**Primary key:** `SERVICE_PLAN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERVICE_PLAN_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the service plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_TRAIL_REVISION` | INTEGER |  | The revision in which this update was made. Corresponds with a line of SERVICE_PLAN_HX_REVISION. |
| 4 | `AUDIT_TRAIL_ITEM` | VARCHAR |  | The number of the item that was updated |
| 5 | `AUDIT_TRAIL_LINE` | INTEGER |  | The line of the item in AUDIT_TRAIL_ITEM being updated. 1 for single response items. |
| 6 | `AUDIT_TRAIL_NEW_VALUE` | VARCHAR |  | The new value of the item in AUDIT_TRAIL_ITEM at the line in AUDIT_TRAIL_LINE, after the update is made. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SERVICE_PLAN_ID` | [SERVICE_PLAN](SERVICE_PLAN.md) | sole_pk | high |

