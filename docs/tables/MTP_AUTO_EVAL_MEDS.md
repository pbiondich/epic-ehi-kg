# MTP_AUTO_EVAL_MEDS

> Medication information obtained from the Medication Therapy Opportunities Engine.

**Primary key:** `PROBLEM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the med therapy problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 4 | `ORDER_MED_ID` | NUMERIC | FK→ | The order for the medication identified by the medication therapy opportunities engine evaluation. |
| 5 | `PROB_MED_SOURCE_C_NAME` | VARCHAR |  | The source of the medication identified by the medication therapy opportunities engine evaluation. |
| 6 | `MED_FILED_DATE` | DATETIME |  | The date when the medication information was filed. This is generally either the date that the medication was started or the date when the medication was dispensed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

