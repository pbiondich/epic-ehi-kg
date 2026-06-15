# NAV_ACTORD_AUD_TRL

> Table for inpatient navigator active orders audit trail.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IP_NAV_AUDIT_USR_ID` | VARCHAR |  | The unique identifier of the user who viewed or took an action on the order. |
| 4 | `IP_NAV_AUDIT_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `IP_NAV_AUDIT_DTTM` | DATETIME (Local) |  | The instant an action was taken on an order record. |
| 6 | `IP_NAV_AUDIT_ACTN_C_NAME` | VARCHAR |  | The action category ID for the order record, indicating the action taken in an inpatient navigator. |
| 7 | `IP_NAV_AUDIT_CTXT_C_NAME` | VARCHAR |  | The context category ID for the order record, indicating the type of navigator in which an action was taken. |
| 8 | `IP_NAV_AUDIT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

