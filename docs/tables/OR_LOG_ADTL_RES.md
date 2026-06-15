# OR_LOG_ADTL_RES

> The OR_LOG_ADTL_RES table contains OR management system log additional resource requests.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log for which there are additional resources. |
| 2 | `LINE` | INTEGER | PK | The line number of the additional resource. |
| 3 | `ADTL_RES` | VARCHAR |  | The free text request for additional equipment, instruments, implants, or supplies. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

