# OR_LOG_ANES_TECH

> The OR_LOG_ANES_TECH table contains OR management system log anesthesia techniques.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log referred to by the anesthesia techniques. |
| 2 | `LINE` | INTEGER | PK | The line of the anesthesia special techniques used in the surgical log. |
| 3 | `ANESTH_SPEC_TECH_C_NAME` | VARCHAR | org | The category value which refers to any special techniques that were required when administering the anesthesia in the surgery in the surgical log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

