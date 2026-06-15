# ORDER_RES_COMP_CMT

> This table contains result component value comments for orders that are populated by the Incoming Results Interface. These result component value comments are not populated through Enter/Edit Results. The data in this table is only populated if the result component value normally stored in the Value_Internal (I ORD 2010) item (ORDER_RESULTS.ORD_VALUE or ORDER_RESULTS.ORD_NUM_VALUE) is too long to be stored in that item.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE_COMP`, `LINE_COMMENT`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The order ID for this order/procedure. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE_COMP` | INTEGER | PK | The line count associated with the result component. This line number will match with the LINE column in the ORDER_RESULTS table. It is probable that this table will not have all the lines from the ORDER_RESULTS table since this table only contains data for the components that do not have data in item that stores the result component in the Order record. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `COMPONENT_ID` | NUMERIC | shared | The unique ID of each result component for each result. Additional data about result components can be found in the CLARITY_COMPONENT table. |
| 6 | `COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |
| 7 | `LINE_COMMENT` | INTEGER | PK | The line count associated with each line of the result component comments. There can be multiple lines of comments, therefore each line has a line number. |
| 8 | `CM_CT_OWNER_ID` | VARCHAR |  | The contact owner deployment of this record; used in Community Model record sharing. |
| 9 | `RESULTS_COMP_CMT` | VARCHAR |  | The result component value comments for this order record which are populated by the Incoming Results Interface. These result comments are NOT populated by Enter/Edit Results. This column is populated when the result component values that are normally stored in the result component in the Order record (ORDER_RESULTS.ORD_VALUE or ORDER_RESULTS.ORD_NUM_VALUE) are too long to be stored in the result component in the Order record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

