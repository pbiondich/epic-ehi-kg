# ORDER_CUMULATIVE_DOSE

> Cumulative dose information for the order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TYPE_C_NAME` | VARCHAR |  | The cumulative dose type |
| 4 | `ORDERED_FROM_CONV_YN` | VARCHAR |  | Did the ordered value come from a conversion? |
| 5 | `ORDERED_VALUE` | NUMERIC |  | The ordered value for the cumulative dose type |
| 6 | `LAST_CALCULATED_VALUE` | NUMERIC |  | The last calculated value for the cumulative dose type |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

