# PR_EST_NOTIF

> This tables stores the notifications sent for estimate records.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTIF_DTTM` | DATETIME (UTC) |  | Stores the UTC instant when the notification was sent for this estimate. |
| 4 | `NOTIF_HX_DESTTYPE_C_NAME` | VARCHAR |  | The type of notification that was sent (e.g. Email/SMS). |
| 5 | `NOTIF_DEST` | VARCHAR |  | The destination (email or phone number) to which an estimate notification was sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

