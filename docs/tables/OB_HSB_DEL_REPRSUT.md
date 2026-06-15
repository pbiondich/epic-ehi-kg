# OB_HSB_DEL_REPRSUT

> This table contains information about the repair suture used to repair episiotomies or lacerations during the delivery for this pregnancy.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID assigned to the episode record (HSB .1). |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `OB_DEL_REPAIR_SUT_C_NAME` | VARCHAR | org | This item stores the repair suture type used in repairing episiotomies or lacerations during the delivery. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

