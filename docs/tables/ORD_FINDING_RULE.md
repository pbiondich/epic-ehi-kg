# ORD_FINDING_RULE

> Clarity table for the ORD 54430 related group, which stores rules and rule outcomes for structural heart patient identification.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FINDING_RULE_ID` | VARCHAR |  | Stores the rule that was evaluated with the order. |
| 4 | `FINDING_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 5 | `FINDING_RULE_EVALUATION_YN` | VARCHAR |  | Stores what the actionable finding rule on the order evaluated to. |
| 6 | `FIND_RULE_NLP_OUTCOME_C_NAME` | VARCHAR |  | Stores the confusion matrix outcome for the rule, calculated by comparing what the rule evaluated and what findings currently exist on the order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

