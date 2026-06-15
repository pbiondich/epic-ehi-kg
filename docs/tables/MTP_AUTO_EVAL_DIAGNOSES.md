# MTP_AUTO_EVAL_DIAGNOSES

> The diagnosis information obtained from the Medication Therapy Opportunities Engine.

**Primary key:** `PROBLEM_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the med therapy problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUTO_EVAL_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `PROB_DIAG_SOURCE_C_NAME` | VARCHAR |  | The source of the diagnosis identified by the medication therapy opportunities engine evaluation. |
| 5 | `PROBLEM_LIST_ID` | NUMERIC | FK→ | The problem list identified by the medication therapy opportunities engine evaluation. |
| 6 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The patient encounter associated with the diagnosis identified by the medication therapy opportunities engine evaluation. |
| 7 | `INVOICE_ID` | NUMERIC | FK→ | The invoice associated with the diagnosis identified by the medication therapy opportunities engine evaluation. |
| 8 | `SURGICAL_LOG_ID` | VARCHAR |  | The surgical log associated with the diagnosis identified by the medication therapy opportunities engine evaluation. |
| 9 | `SURGICAL_CASE_ID` | VARCHAR |  | The surgical case associated with the diagnosis identified by the medication therapy opportunities engine evaluation. |
| 10 | `DX_DATE_FILED_DATE` | DATETIME |  | The date when the diagnosis information was filed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

