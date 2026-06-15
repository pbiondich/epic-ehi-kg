# PEND_PRED_DEPT

> This table contains predicted next destination units for pend (PND) records based on predictive models.

**Primary key:** `PEND_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PEND_ID` | VARCHAR | PK FK→ | The unique identifier for the pended entry record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PRED_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 4 | `PRED_DEPT_CONF_NUM` | NUMERIC |  | The percent confidence from the predictive model for each of the predicted next destination units. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PEND_ID` | [PEND_ACTION](PEND_ACTION.md) | sole_pk | high |

