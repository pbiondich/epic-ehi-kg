# ORD_AUD_PROTCL_OWNER

> This table contains audit information about the owner that the protocol was assigned to for protocolling.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OWN_PROTCL_GROUPER_C` | INTEGER |  | This audit trail item stores imaging protocol owners. Protocols can be reassigned and routed to providers pools or protocol categories. |
| 4 | `OWN_PROTCL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `OWN_PROTCL_POOL_ID` | VARCHAR |  | This audit trail column stores imaging protocol owners. This column stores the pools that were assigned. The source item is located at ORDER_PROC_3.PROTCL_ASGN_POOL_ID. |
| 6 | `OWN_PROTCL_POOL_ID_POOL_NAME` | VARCHAR |  | The name of the scheduling pool used when searching for available providers for an appointment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

