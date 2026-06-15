# PROB_TXP_MODIFIERS

> Table of modifiers related to transplant problems.

**Primary key:** `PROBLEM_LIST_ID`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique ID of this Problem List entry. |
| 2 | `BIOPSY_C_NAME` | VARCHAR | org | Shows whether a biopsy was done to confirm organ rejection. If a biopsy was performed, this column will display "yes." If not, the column will be blank. |
| 3 | `STENT_INSERTED_YN` | VARCHAR |  | Indicates whether or not a stent has been inserted due to a bronchial stricture. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

