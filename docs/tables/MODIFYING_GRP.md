# MODIFYING_GRP

> Table for storing modifying user, instant and acknowledged instant.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MODIFYING_USER_ID` | VARCHAR |  | The unique ID of the user who modified the order. |
| 4 | `MODIFYING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `MOD_DTTM` | DATETIME (Local) |  | Stores the instant when an inpatient order is modified. |
| 6 | `MOD_ACK_DTTM` | DATETIME (Local) |  | Stores the instant when a modified order is acknowledged. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

