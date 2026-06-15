# AUD_PUMP_PROG

> The AUD_PUMP_PROG table contains audit trail information about infusion pump programming messages received back from the pumps.

**Primary key:** `ALERT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the med alert record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `E_INF_SEND_INS_DTTM` | DATETIME (UTC) |  | Audit trail for the instant when the pump program was sent to the infusion pump. |
| 4 | `E_INF_RESPONSE_DTTM` | DATETIME (UTC) |  | Audit trail for the instant when the response was received from the infusion pump. |
| 5 | `E_INF_ADMIN_IN_DTTM` | DATETIME (Local) |  | Tracks the administration instant with the pump order details audit trail |
| 6 | `E_INF_ATTEMPT_UTC_DTTM` | DATETIME (UTC) |  | Tracks the instant the user attempted to program the pump in the audit trail |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

