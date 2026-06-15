# FIN_ASST_CASE_EXPENSE

> This table contains expense information related to a financial assistance case record.

**Primary key:** `FIN_ASST_CASE_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier for the financial assistance case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXPENSE_TYPE_C_NAME` | VARCHAR | org | The expense type category ID. |
| 4 | `EXPENSE_FREQ_C_NAME` | VARCHAR |  | The category ID of frequency with which this expense occurs. |
| 5 | `EXPENSE_AMOUNT` | NUMERIC |  | The expense amount per frequency. |
| 6 | `EXP_BLNG_PAT_RELATIONSHIP_ID` | NUMERIC |  | The patient contact of one of the patients on the case for whom the expense information in the current row belongs to. If the information belongs to a patient on the case, EXPENSE_BELONGS_TO_PAT_ID column will be set instead. |
| 7 | `EXPENSE_COMMENT` | VARCHAR |  | A brief comment about the expense information in the current row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

