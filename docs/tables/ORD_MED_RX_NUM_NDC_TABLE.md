# ORD_MED_RX_NUM_NDC_TABLE

> This table contains the prescription numbers associated with NDC records when the pharmacy sends multiple adjudication messages for unique NDCs, without including the compound segment in the adjudication message.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RX_NUMBER_RAW` | VARCHAR |  | Stores the compiled prescription number for each NDC when the pharmacy sends multiple adjudication messages for unique NDCs, without including the compound segment in the adjudication message. |
| 4 | `RX_NUMBER` | VARCHAR |  | Stores the formatted prescription number for each NDC when the pharmacy sends multiple adjudication messages for unique NDCs, without including the compound segment in the adjudication message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

