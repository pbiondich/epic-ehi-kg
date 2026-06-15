# PR_EST_TEMPLATES_USED

> Contains list of templates used in a price estimate.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PR_EST_TEMPLATE_ID` | NUMERIC | FK→ | Templates used to create the estimate. |
| 4 | `PR_EST_TEMPLATE_ID_PR_EST_TEMPLATE_NAME` | VARCHAR |  | The name of the estimate template record. |
| 5 | `PR_EST_TEMPLATE_CSN_ID` | NUMERIC |  | Contains the template CSN used for producing the estimate. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PR_EST_TEMPLATE_ID` | [PR_EST_TEMPLATE](PR_EST_TEMPLATE.md) | sole_pk | high |

