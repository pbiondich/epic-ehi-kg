# ORDER_RES_AUDIT_VALS

> The table ORDER_RES_AUD_VALS stores multiple, modified values for an item in audit related group.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated audit data in the result finding record. Together with FINDING_ID, this forms the foreign key to the ORDER_RES_AUDIT table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple item values that are associated with the item from the table ORDER_RES_AUDIT. |
| 4 | `AUDIT_VALUE` | VARCHAR |  | This column stores the values of the item being audited as specified in this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

