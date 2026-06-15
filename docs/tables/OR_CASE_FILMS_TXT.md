# OR_CASE_FILMS_TXT

> This table contains the free text films information for the surgical case (ORC) record.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique ID of the procedural case record. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `FILMS_FOR_SURGERY` | VARCHAR |  | List of films that the patient will be bringing to surgery. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

