# RES_MICRO_CULTURE_BILL_SS

> This table contains additional procedures that were charged when this result was last processed by billing.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated isolate in this culture result. Together with RESULT_ID, this forms the foreign key to the RES_MICRO_CULTURE table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple billing snapshots associated with the result and the isolate from the RES_MICRO_CULTURE table. |
| 4 | `CULTURE_BILL_SS` | VARCHAR |  | The billing snapshot of all billing procedures and quantities for an isolate result when this result was last processed by billing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

