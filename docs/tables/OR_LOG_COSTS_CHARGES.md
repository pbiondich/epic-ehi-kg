# OR_LOG_COSTS_CHARGES

> The OR_LOG_COSTS_CHARGES table contains information about costs and charges associated with the procedural log.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COST_CHARGE_TYPE_C_NAME` | VARCHAR |  | The cost and charge type category ID for the procedural log. |
| 4 | `CASE_COST` | NUMERIC |  | The cost amount of the associated type for the procedural log. |
| 5 | `CASE_CHARGE` | NUMERIC |  | The charge amount sent for the associated type for the procedural log. The charge is determined using the necessary settings from the procedural location and the relevant charge settings in place at the time the charges were triggered. Note that this value may differ from what is actually sent from the billing system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

