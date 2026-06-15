# PR_EST_EVALUATION_INFO

> Rule evaluation information for the price estimate for checking what warnings and calculations were performed.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EVAL_RULE_ID` | VARCHAR |  | Stores rules that impacted the estimate at some point in its lifecycle. These can be warning rules to advise user behavior or calculation rules that changed amounts. |
| 4 | `EVAL_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 5 | `EVAL_RULE_TYPE_C_NAME` | VARCHAR |  | Stores the type of rule that was evaluated for the estimate. |
| 6 | `PR_EST_EVAL_STATE_C_NAME` | VARCHAR |  | Stores the latest state of the rule that from when it was last evaluated for the estimate. |
| 7 | `EVAL_UPDATE_INST_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant this line was last updated, either by being added to the estimate, the state being changed, or affected dental procedures changing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

