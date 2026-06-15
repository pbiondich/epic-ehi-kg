# FIN_ASST_CASE_ASSOC_PAT

> This table contains information about the patients on a financial assistance case record.

**Primary key:** `FIN_ASST_CASE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier for the financial assistance case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASSOC_PAT_ID` | VARCHAR | FK→ | The unique ID of the patient associated with the financial assistance case record. |
| 4 | `CHILD_FIN_ASST_CASE_ID` | NUMERIC |  | This item stores the ID of a child financial assistance case record. This child record is used to store the patient specific SmartForm information for the associated patient in the related group. |
| 5 | `MYC_SELECTED_YN` | VARCHAR |  | Flag set when the patient was added to the online application. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ASSOC_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

