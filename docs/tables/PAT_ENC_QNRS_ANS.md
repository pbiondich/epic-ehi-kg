# PAT_ENC_QNRS_ANS

> The PAT_ENC_QNRS_ANS table contains the Answer ID numbers for the Answers to all Appointment Questionnaires. An Appointment can have multiple Questionnaires that are used in conjunction with it, and each Questionnaire will have one Answer record associated with it.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | This is the Contact Serial Number. It uniquely identifies this contact across all patients and all contacts. |
| 2 | `LINE` | INTEGER | PK | This item stores the line number of each Questionnaire Answer record that exists for this record. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

