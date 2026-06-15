# TASK_ORD_LINK

> The Clarity table tracks orders linked to patient medication reminders. This data allows customers to understand how order changes affect medication reminder adherence in the larger picture of medication reminders being reused for associated orders.

**Primary key:** `ACTIVITY_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OUTPAT_ORD_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant a new order was linked to the patient assigned medication reminder in UTC. |
| 4 | `OUTPAT_ORDER_ID` | NUMERIC |  | All orders linked to a medication reminders in order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

