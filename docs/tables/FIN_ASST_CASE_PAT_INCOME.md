# FIN_ASST_CASE_PAT_INCOME

> This table contains income-related information for a financial assistance record, as reported by the patient.

**Primary key:** `FIN_ASST_CASE_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_INCOME_TYPE_C_NAME` | VARCHAR | org | This item stores the types of income sources entered by the patient. |
| 4 | `PAT_INCOME_FREQ_C_NAME` | VARCHAR |  | How often the income is received entered by the patient. |
| 5 | `PAT_INCOME_HOURS_PER_WEEK` | NUMERIC |  | If income is hourly, the number of hours per week entered by the patient. |
| 6 | `PAT_INCOME_AMOUNT` | NUMERIC |  | This item stores the income earned per frequency entered by the patient. |
| 7 | `PAT_INCOME_COMMENT` | VARCHAR |  | This item stores the comment entered by a patient for the current income information row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

