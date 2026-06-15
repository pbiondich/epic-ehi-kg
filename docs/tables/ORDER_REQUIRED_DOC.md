# ORDER_REQUIRED_DOC

> This table stores information about the documentation required by the external resulting agency for this Orders and Results Network procedure.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REQ_INFO_QUESTION_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 4 | `REQUIREMENT_STATUS_C_NAME` | VARCHAR |  | The Required Information Status category value corresponding to the fulfillment of the requirement in REQ_INFO_NET_IDENT on this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

