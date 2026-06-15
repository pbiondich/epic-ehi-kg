# ORDER_COND_QUESNS

> The ORDER_COND_QUESNS table contains the inpatient condition questions (if configured) for an order

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COND_QUESN_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 4 | `COND_QUESN_DAT` | NUMERIC |  | The contact date of the question record that identifies the condition question for an inpatient order. |
| 5 | `COND_QUESN_RESP` | VARCHAR |  | The response to a condition question for an inpatient order |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

