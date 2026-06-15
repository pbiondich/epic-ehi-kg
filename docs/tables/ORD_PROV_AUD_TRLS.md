# ORD_PROV_AUD_TRLS

> This table stores the authorizing provider audit trail for orders.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PROV_AUDIT_USER_ID` | VARCHAR |  | The unique user ID of the authorizing provider from the audit trail. |
| 4 | `PROV_AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `PROV_AUDIT_INSTANT` | DATETIME (Local) |  | The instant that the associated authorizing provider was recorded in the order record. |
| 6 | `PROV_AUDIT_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `PROV_AUDIT_POOL_ID` | NUMERIC |  | The unique identifier for registry record representing the group of users who are responsible for a cosignature requirement on the order record. |
| 8 | `PROV_AUDIT_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 9 | `PROV_AUDIT_TYPE_C_NAME` | VARCHAR |  | The type of provider from the audit trail. |
| 10 | `PROV_AUDIT_ACTION_C_NAME` | VARCHAR |  | The action from the audit trail. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

