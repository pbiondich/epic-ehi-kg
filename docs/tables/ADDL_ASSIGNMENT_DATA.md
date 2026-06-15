# ADDL_ASSIGNMENT_DATA

> Clarity table for additional assignment data.

**Primary key:** `ASGN_DATA_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ASGN_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the assignment data record record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDL_ASSIGNMENT_ITEM_TYPE_C_NAME` | VARCHAR | org | Additional Data Type Description. |
| 4 | `ADDL_ASSIGNMENT_ITEM_CODE` | VARCHAR |  | Stores the additional item code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ASGN_DATA_ID` | [ASSIGNMENT_DATA](ASSIGNMENT_DATA.md) | sole_pk | high |

