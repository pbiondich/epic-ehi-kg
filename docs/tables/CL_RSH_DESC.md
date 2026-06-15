# CL_RSH_DESC

> This table contains the description text of research study and client records.

**Primary key:** `RESEARCH_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Each description will have its own line number. |
| 3 | `DESCRIPTION` | VARCHAR |  | The research study or client description, which may be divided across multiple rows in this table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

