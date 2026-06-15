# PR_EST_TEMPLATE

> The PR_EST_TEMPLATE table contains basic information about estimate template records, such as what the records are called, who created them, when they were created, when they should be retired, and what activity they are applicable for.

**Primary key:** `PR_EST_TEMPLATE_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PR_EST_TEMPLATE_ID` | NUMERIC | PK | The unique identifier for the estimate template record. |
| 2 | `PR_EST_TEMPLATE_ID_PR_EST_TEMPLATE_NAME` | VARCHAR |  | The name of the estimate template record. |
| 3 | `PR_EST_TEMPLATE_NAME` | VARCHAR |  | The name of the estimate template record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [PR_EST_TEMPLATES_USED](PR_EST_TEMPLATES_USED.md) | `PR_EST_TEMPLATE_ID` | high |

