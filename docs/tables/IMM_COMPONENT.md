# IMM_COMPONENT

> This Clarity table contains immunization component administration data.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier (I LPL .1) for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMM_COMP_TYPE_C_NAME` | VARCHAR |  | Indicates the type of the immunization component. Used for multiple component immunization administrations and additional administration data that needs to be documented with the same vaccine event. |
| 4 | `IMM_COMP_NDC_ID` | VARCHAR |  | Stores the NDC of the additional immunization data. |
| 5 | `IMM_COMP_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 6 | `IMM_COMP_LOT_NUM` | VARCHAR |  | Stores the lot number of the additional immunization component. |
| 7 | `IMM_COMP_LOT_NUM_ID_LOT_NUM` | VARCHAR |  | The lot number on the vial for a given medication or immunization. |
| 8 | `IMM_COMP_EXP_DATE` | DATETIME |  | Stores the expiration date of the additional immunization component. |
| 9 | `IMM_COMP_INVENTORY_CLASS_C_NAME` | VARCHAR |  | Stores the inventory class of lot documented for the additional immunization component. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

