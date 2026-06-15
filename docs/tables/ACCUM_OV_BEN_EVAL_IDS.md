# ACCUM_OV_BEN_EVAL_IDS

> The benefit evaluators whose payment mechanisms were used in place of those on the source benefit evaluator when computing applied amounts for a transaction.

**Primary key:** `ACCUMULATION_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCUMULATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the accumulation record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OV_BEN_EVAL_ID` | NUMERIC |  | The benefit evaluators whose payment mechanisms were used to override those on the source benefit evaluator. In some cases, the override itself may be overridden. For example, if a payment would accumulate to the deductible, but the MOOP has already been met, the core payment would be overridden by the deductible, which would then be overridden by the MOOP. In such cases, the benefit evaluator in line N overrides the one in line N-1. In this example, line 1 would contain the deductible, and line 2 would contain the MOOP. |
| 4 | `OV_BEN_EVAL_ID_BEN_EVAL_NAME` | VARCHAR |  | The name of the benefit evaluator record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

