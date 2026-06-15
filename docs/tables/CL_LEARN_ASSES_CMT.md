# CL_LEARN_ASSES_CMT

> This table contains patient learning assessment comments.

**Primary key:** `LEARNING_ASSMT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LEARNING_ASSMT_ID` | NUMERIC | PK FK→ | The unique ID for the patient learning assessment record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The contact date in external format. |
| 5 | `ASSMT_CMT` | VARCHAR |  | The comment for learning assessment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LEARNING_ASSMT_ID` | [CL_LEARN_ASSESS_NS](CL_LEARN_ASSESS_NS.md) | sole_pk | high |

