# OR_CASE_INF_STAT

> The OR_CASE_INF_STAT table contains OR management system case patient infection status.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the infection status information for the case. |
| 3 | `INFECTION_STAT_C_NAME` | VARCHAR | org | The category value which indicates the type of infection status associated with the patient in the case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

