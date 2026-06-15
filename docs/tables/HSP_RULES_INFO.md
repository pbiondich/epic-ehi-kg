# HSP_RULES_INFO

> The HSP_RULES_INFO table contains information about hospital billing workqueue rules.

**Primary key:** `RULE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RULE_ID` | NUMERIC | PK shared | This column stores the unique identifier for the rule record. |
| 2 | `RULE_ID_RULE_NAME` | VARCHAR |  | This column stores the name of the hospital billing workqueue rule. |
| 3 | `RULE_NAME` | VARCHAR |  | This column stores the name of the hospital billing workqueue rule. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

