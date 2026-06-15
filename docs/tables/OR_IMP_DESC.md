# OR_IMP_DESC

> The OR_IMP_DESC table contains OR management system implant descriptions.

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique ID of the implant record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the description information for the implant. |
| 3 | `DESCRIPTION` | VARCHAR |  | One line of description of the implant record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

