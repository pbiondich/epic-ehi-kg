# MED_THERAPY_PROB_RECOMMND

> This table contains the recommendation to resolve a problem.

**Primary key:** `PROBLEM_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the med therapy problem record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `MTP_RECOMMEND_C_NAME` | VARCHAR | org | The recommended action category ID for the medication therapy problem. |
| 5 | `RECOMMENDED_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 6 | `RECOMMENDED_MED_COMMENTS` | VARCHAR |  | The recommended medication comments include additional information entered by the user who documented the medication therapy problem. |
| 7 | `MTP_OUTCOME_C_NAME` | VARCHAR | org | The outcome category ID for the medication therapy problem. |
| 8 | `MED_TO_ACT_ON_ORDER_ID` | NUMERIC |  | The unique ID of the existing medication order that the recommended action applies to. |
| 9 | `MED_TO_ACT_ON_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 10 | `RECOMMENDED_MED_ORDER_ID` | NUMERIC |  | The unique ID of the medication order that should be signed to complete the recommendation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

