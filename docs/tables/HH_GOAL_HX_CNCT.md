# HH_GOAL_HX_CNCT

> This table stores goal history information for Home Health & Hospice care plan contacts.

**Primary key:** `GOAL_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GOAL_ID` | VARCHAR | PK FK→ | The unique identifier for the goal record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_CSN` | VARCHAR |  | This item specifies the patient contact associated with a goal visit note addendum. |
| 4 | `HX_ADDENDUM_LN` | INTEGER |  | This item specifies the addendum number for the contact specified in the Goals information (I IGO 27500) field. |
| 5 | `HX_OUTCOME_C_NAME` | VARCHAR | org | This item stores historical values of the outcome as of each addendum. |
| 6 | `HX_NOTES_CONTACT` | VARCHAR |  | This item tracks the goal's visit notes contact number (I HNO 10) field on a per-addendum basis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |

