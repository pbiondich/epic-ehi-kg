# ORD_SPEC_QUEST

> This table contains order specific questions and their responses.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line item for this record determined by the order specific question ID |
| 3 | `ORD_QUEST_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 4 | `ORD_QUEST_DATE` | DATETIME |  | The date of the question for this order. |
| 5 | `IS_ANSWR_BYPROC_YN` | VARCHAR |  | Indicates whether or not this question was answered by the procedure. 'Y' indicates that the question was answered. 'N' indicates that the question was not answered. |
| 6 | `ORD_QUEST_COMP` | INTEGER |  | The line number of the medication in the mixture that triggers this specific question for an IV or total parenteral nutrition (TPN) order. |
| 7 | `ORD_QUEST_RESP` | VARCHAR |  | The response to the question for this order. |
| 8 | `ORD_QUEST_CMT` | VARCHAR |  | The comments on the question of the order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

