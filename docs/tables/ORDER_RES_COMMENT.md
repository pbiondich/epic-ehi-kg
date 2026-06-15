# ORDER_RES_COMMENT

> This table contains result component comments for orders that are populated by the Incoming Results Interface. These result component comments are not populated through Enter/Edit Results. The data in this table is populated only if the result component comments normally stored in the Component Comment (I ORD 2070) field is too long to be stored in that field.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`, `LINE_COMMENT`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The internal order ID for this procedure. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line count associated with the result component. This line number will match with the LINE column in the ORDER_RESULTS table. It is probable that this table will not have all the lines from the ORDER_RESULTS table since this table only contains data for the components that do not have data in the Component Comment item in the Order record (ORDER_RESULTS.COMPONENT_COMMENT). |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | ID of the deployment owner for this contact. This relates to record sharing and who owns the deployment of the record. |
| 6 | `RESULTS_CMT` | VARCHAR |  | The result component comments for this order record which are populated by the Incoming Results Interface. These result comments are not populated by Enter/Edit Results. This column is populated when the result component comments that are normally stored in the Component Comment item in the Order record (ORDER_RESULTS.COMPONENT_COMMENT) are too long to be stored in the Component Comment item in the Order record. |
| 7 | `COMPONENT_ID` | NUMERIC | shared | The unique ID of each result component for each result. Additional data about result components can be found in the CLARITY_COMPONENT table. |
| 8 | `COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |
| 9 | `LINE_COMMENT` | INTEGER | PK | The line count associated with each line of the result component comments. There can be multiple lines of comments, therefore each line has a line number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

