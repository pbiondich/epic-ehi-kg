# PHARM_EXPECTED_WKFL_STEPS

> This table contains the list of pharmacy workflow steps that were not completed.

**Primary key:** `ALERT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the med alert record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXPECT_RX_WORKFLOW_STEP_C_NAME` | VARCHAR |  | The expected pharmacy workflow step category ID for the med alert. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

