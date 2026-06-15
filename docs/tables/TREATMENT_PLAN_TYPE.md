# TREATMENT_PLAN_TYPE

> Indicates which types of treatment plan data are present in the simple generic record.

**Primary key:** `MED_PRBLM_LIST_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_PRBLM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the medical problem list record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TREAT_PLAN_TYPE_C_NAME` | VARCHAR |  | This captures the activities that use the Treatment Plan structure for this simple generic record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MED_PRBLM_LIST_ID` | [MDL_MD_PRBLM_LIST](MDL_MD_PRBLM_LIST.md) | sole_pk | high |

