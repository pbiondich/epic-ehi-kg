# ORD_RESEARCH_ASSOC_HX

> This table contains information about the changes that have occurred to the association between an order and research studies after an order has been signed. If the research association of an order has not been modified, it will not appear in this table. Each row is one change event for an order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASSOCIATING_USER_ID` | VARCHAR |  | User ID responsible for the change on this line of this order. |
| 4 | `ASSOCIATING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ASSOCIATED_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the order had its research association changed after signing. |
| 6 | `RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 7 | `PREV_RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 8 | `RSH_CODE_FROM_C_NAME` | VARCHAR |  | This column stores the source that was used to modify the research association of this order in this modification event. |
| 9 | `PREV_RSH_CODE_FROM_C_NAME` | VARCHAR |  | This column stores the source that was used to modify the research association in the previous modification event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

