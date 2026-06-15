# IMG_LOAD_BALANCE_AUDIT

> This table holds information about the actions the Radiant Load Balancer took on studies at each instant in time.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LD_BALANCE_ACTION_C_NAME` | VARCHAR |  | The specific action taken on an order by the Load Balancer at a given instant in time. |
| 4 | `LD_BALANCE_STDY_PRI` | INTEGER |  | The priority score of the study at a given instant in time. |
| 5 | `LD_BALANCE_ACN_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant in time at which a load balancing event took place. |
| 6 | `LD_BALANCE_ADT_USER_ID` | VARCHAR |  | The user who initiated a load balancing action such as reassigning a study to another provider, returning a study for redistribution, or signing a study. |
| 7 | `LD_BALANCE_ADT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

