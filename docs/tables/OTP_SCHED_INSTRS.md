# OTP_SCHED_INSTRS

> The scheduling instructions for an order template.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The order template ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to a line of scheduling instructions for the order template in this row. |
| 3 | `ORDER_SCHED_INSTR` | VARCHAR |  | A line of the scheduling instructions for the order template in this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

