# ORTHO_TREAT_NOTE

> The ORTHO_TREAT_NOTE table contains information about orthodontics treatment note.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | VARCHAR | PK shared | The unique identifier for the treatment plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTE` | VARCHAR |  | Printable comments for the treatment plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

