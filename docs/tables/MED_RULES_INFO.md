# MED_RULES_INFO

> This table contains the basic no-add information for medication alert rules.

**Primary key:** `MED_RULE_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_RULE_ID` | NUMERIC | PK | The unique identifier for the rule record. |
| 2 | `MED_RULE_ID_MED_RULE_NAME` | VARCHAR |  | The name of the alert rule which contains the name of the drug with which the alert is associated with. |
| 3 | `MED_RULE_NAME` | VARCHAR |  | The name of the alert rule which contains the name of the drug with which the alert is associated with. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [RX_INTERVENTION](RX_INTERVENTION.md) | `MED_RULE_ID` | high |

