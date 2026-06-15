# HSP_QI_ELIXHAUSER_COMORB

> The Elixhauser comorbidity categories for hospital accounts. This table contains the comorbidity values used to calculate the comorbidity index, not the comorbidity index values.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ELIXHAUSER_COMORB_C_NAME` | VARCHAR |  | This category list contains AHRQ Elixhauser comorbidity category values for a hospital account. This is not the comoribidty index, but the categories of comorbidities that contribute to the index. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

