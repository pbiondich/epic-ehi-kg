# OTP_ORDER_SPEC_QST

> The order specific questions for an order template.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The order template ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to each order specific question in the order template in this row. |
| 3 | `ORD_SPEC_QUESN_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 4 | `ORD_SPEC_QUESN_DT` | NUMERIC |  | The contact date of an order specific question in the order template in this row. |
| 5 | `ORD_SPEC_QUESN_RESP` | VARCHAR |  | The response to an order specific question in the order template in this row. |
| 6 | `ORD_SPEC_QUESN_CMT` | VARCHAR |  | The comment on an order specific question in the order template in this row. |
| 7 | `IS_ANSWR_BYPROC_YN` | VARCHAR |  | The Y/N flag for whether or not the question in the order template in this row should be answered per procedure. |
| 8 | `ORD_SPEC_QUESN_COMP` | NUMERIC |  | The order specific question component for the order template in this row. |
| 9 | `ORD_SPEC_QUESN_DTE` | NUMERIC |  | The contact date in decimal format of the question. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

