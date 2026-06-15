# OR_LOG_ANESTH_QUAL

> The OR_LOG_ANESTH_QUAL table contains OR management system log anesthesia qualifiers.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log the anesthesia qualifier refers to. |
| 2 | `LINE` | INTEGER | PK | The line number of the anesthesia qualifier in the surgical log. |
| 3 | `ANESTH_QUALIFIER_C_NAME` | VARCHAR | org | The category value which represents the anesthesia qualifier in the surgical log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

