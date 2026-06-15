# REMOVED_PROTOCOLS

> This table links Cell Therapy treatment plans to protocols that were removed from the plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REMOVE_PROTOCOL_ID` | NUMERIC |  | Stores protocols removed from the plan. |
| 4 | `REMOVE_PROTOCOL_ID_PROTOCOL_NAME` | VARCHAR |  | The SmartSet/Protocol record name. This is different from the display name, which is stored in CL_PRL_SS_OT.DISPLAY_NAME. |
| 5 | `REMOVED_REASON` | VARCHAR |  | The reason the associated protocol was removed from the plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

