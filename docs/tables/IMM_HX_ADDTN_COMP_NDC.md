# IMM_HX_ADDTN_COMP_NDC

> This Clarity table contains the auditing data of immunization component NDC for an immunization administration record.

**Primary key:** `PROBLEM_LIST_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the problem record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `IMM_HX_COMP_NDC_ID` | VARCHAR |  | Stores the audit data of the NDC of the additional immunization component. |
| 5 | `IMM_HX_COMP_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

