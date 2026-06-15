# MC_PRICER_FEE_SCHED_ADJ

> Adjustments to CMS Fee Schedule rates determined by the Epic Pricer. Each row indicates one adjustment made to the fee schedule rate for a service.

**Primary key:** `PRICER_MSG_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the pricer message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FEE_SCHEDULE_ADJ_TYPE_C_NAME` | VARCHAR |  | Type of adjustment applied to the CMS fee schedule rate. |
| 4 | `FEE_SCHEDULE_ADJ_PERCENT` | NUMERIC |  | Percentage adjustment to the CMS fee schedule rate for a service. |
| 5 | `FEE_SCHEDULE_ADJ_AMOUNT` | NUMERIC |  | Adjustment to the CMS fee schedule rate for a service. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

