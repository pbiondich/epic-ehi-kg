# PEND_PRED_LOC_GRP

> This table contains predicted next destination level of care groupers for pend (PND) records based on predictive models.

**Primary key:** `PEND_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PEND_ID` | VARCHAR | PK FK→ | The unique identifier for the pended entry record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PRED_LOC_GRP_C_NAME` | VARCHAR | org | The predicted next destination level of care groupers for pending event records based on predictive models. |
| 4 | `PRED_LOC_CONF_NUM` | NUMERIC |  | The percent confidence from the predictive model for each of the predicted next destination level of care groupers. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PEND_ID` | [PEND_ACTION](PEND_ACTION.md) | sole_pk | high |

