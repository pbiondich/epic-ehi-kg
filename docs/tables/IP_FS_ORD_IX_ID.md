# IP_FS_ORD_IX_ID

> This table stores the orders associated with a flowsheet row in a multiple-response format for easier reporting.

**Primary key:** `INPATIENT_DATA_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique ID of the inpatient data record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated order ID stored in a flowsheet row in this inpatient data record. Together with INPATIENT_DATA_ID, this forms the foreign key to the IP_FLOWSHEET_ROWS table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple order IDs stored in a flowsheet row that is associated with the inpatient data record and the order ID from the IP_FLOWSHEET_ROWS table. |
| 4 | `IX_FLOW_RW_ORD_ID` | NUMERIC |  | The unique IDs of the orders that are added to this patient's flowsheet row. This is a multiple-response item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

