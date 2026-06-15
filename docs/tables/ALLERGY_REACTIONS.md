# ALLERGY_REACTIONS

> The ALLERGY_REACTIONS table contains the category values of the reactions associated with a given allergy. There may be multiple reactions associated with a single allergy. In this case, there will be multiple records in this table with the same ALLERGY_ID, but with different LINE values.

**Primary key:** `ALLERGY_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALLERGY_ID` | NUMERIC | PK FK→ | The unique ID used to identify the allergy record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REACTION_C_NAME` | VARCHAR | org | The integer category value corresponding to the type of allergy reaction. To display names and/or abbreviations, link to the associated ZC lookup table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALLERGY_ID` | [ALLERGY](ALLERGY.md) | sole_pk | high |

