# IMG_LOAD_BALANCE_SRC_RWL

> The table representing the related multi-response item ORD 52871. The data set here corresponds to the reading work lists an order was associated with at a given instant a load balancing action was taken on the order.

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `LD_BALANCE_SRC_REPORT_INFO_ID` | NUMERIC |  | The reading work lists that this order was on at the time a load balancing action took place. |
| 5 | `LD_BALANCE_SRC_REPORT_INFO_ID_REPORT_INFO_NAME` | VARCHAR |  | The name of the report. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

