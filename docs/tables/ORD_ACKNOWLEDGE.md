# ORD_ACKNOWLEDGE

> This table is used to extract inpatient order acknowledge information.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of times the order is acknowledged. |
| 3 | `ACK_TYPE_C_NAME` | VARCHAR |  | The acknowledge type category number for the order. Only Hospital Outpatient Visit (HOV) appointments have a value populated for this column. |
| 4 | `ACK_USER_ID` | VARCHAR |  | The user who marked the order as acknowledged and validated they saw it, and take responsibility for it |
| 5 | `ACK_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `ACK_TIME` | DATETIME (Local) |  | The date and time at which a user acknowledged they had seen the order and take responsibility for it. |
| 7 | `ACK_DETAIL_LINE` | INTEGER |  | This column is used only while acknowledging modified orders. Since an order may be modified multiple times, this column saves the line number for acknowledged modifications from group ORD-35100, which stores the username of the user who modified the order. |
| 8 | `ACK_LINKED_LINE` | INTEGER |  | Stores the line within the Superitem that a given line is linked to. |
| 9 | `AUTO_ACK_YN` | VARCHAR |  | This column stores whether or not an order automatically had a user acknowledge the order and take responsibility for it. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

