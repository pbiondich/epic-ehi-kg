# ORD_ADJ_END_DATE_ACTIONS

> Order end date adjustment action details. Includes information regarding automatic end date adjustments and user actions.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADJ_ENDDT_ACTION_C_NAME` | VARCHAR |  | The category number for the automatic end date adjustment action state. |
| 4 | `ADJ_ENDDT_INST_ADD_DTTM` | DATETIME (UTC) |  | The instant this row was generated. |
| 5 | `ADJ_ENDDT_USER_ID` | VARCHAR |  | The user who took action. |
| 6 | `ADJ_ENDDT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ADJ_ENDDT_ACT_INST_DTTM` | DATETIME (UTC) |  | The instant the user took action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

