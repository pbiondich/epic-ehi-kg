# TRT_BILL_DAY_SRC_INSTANCE

> For a treatment plan created from a linked protocol (PTP) record, this table stores the instance number (or repetition number) for the billing protocol treatment days linked to this clinical day in the treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `BILLING_DAY_SRC_INSTANCE_NUM` | INTEGER |  | For each linked billing protocol treatment day in the TPL_TX_SOURCE_BILLING_CSN table, this column stores the corresponding instance number (or repetition number) represented by this clinical day in the treatment plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

