# GNOM_INTPRT_EFFECTS

> Discrete phenotypic effects predicted by an interpretation.

**Primary key:** `GNOM_INTPRT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GNOM_INTPRT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the interpretation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `PHENOTYPE_EFFECT_TYPE_C_NAME` | VARCHAR |  | Stores the phenotypic effect type. This determines the possible values for Effect Value in I GNI 3001 |
| 5 | `PHENOTYPE_EFFECT_VAL_C_NAME` | VARCHAR |  | Stores the phenotypic effect value of the effect type stored in I GNI 3000. |
| 6 | `ACT_SCORE_LOW` | NUMERIC |  | This item determines the lowest possible value for the activity score. If the activity score is a single value, this and the upper bound are equal to that value. If the activity score is a range and a lower bound is supplied, this item is equal to the lower bound. When the lower bound is not provided as part of the range, this item is equal to the universal lower bound (0). |
| 7 | `ACT_SCORE_UPPER` | NUMERIC |  | This item determines the highest possible value for the activity score. If the activity score is a single value, this and the lower bound are equal to that value. If the activity score is a range and an upper bound is supplied, this item is equal to the upper bound. When the upper bound is not provided as part of the range, this item is equal to the universal upper bound (99999). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GNOM_INTPRT_ID` | [GNOM_INTPRT_IDENT](GNOM_INTPRT_IDENT.md) | sole_pk | high |

