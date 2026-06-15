# FIN_ASST_CASE_PAT_EXPENSE

> This table contains expense information related to a financial assistance case record, as reported by the patient.

**Primary key:** `FIN_ASST_CASE_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_EXPENSE_TYPE_C_NAME` | VARCHAR | org | The type of expense entered by the patient. |
| 4 | `PAT_EXPENSE_FREQ_C_NAME` | VARCHAR |  | How often the expense occurs, as entered by the patient. |
| 5 | `PAT_EXPENSE_AMOUNT` | NUMERIC |  | Amount spent for an expense type entered by the patient. |
| 6 | `PAT_EXPENSE_COMMENT` | VARCHAR |  | Comment entered by a patient for the current expense information row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

