# OR_CASE_ANES_TYPE

> The OR_CASE_ANES_TYPE table contains OR management system case anesthesia types.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The internal ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the anesthesia type within the case. |
| 3 | `ANESTH_TYPES_C_NAME` | VARCHAR | org | The category value which indicates the type of anesthesia being administered during the case. |
| 4 | `ANESTH_LOC_C_NAME` | VARCHAR | org | The category value which indicates the location of the body where the anesthesia will be administered. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

