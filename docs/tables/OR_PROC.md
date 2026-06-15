# OR_PROC

> The OR_PROC table contains OR management system procedures.

**Primary key:** `OR_PROC_ID`  
**Columns:** 3  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_PROC_ID` | VARCHAR | PK | The unique internal ID of the surgical procedure record. |
| 2 | `OR_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 3 | `PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [OR_CASE_ALL_PROC](OR_CASE_ALL_PROC.md) | `OR_PROC_ID` | high |
| [OR_CASE_APPTS_PR](OR_CASE_APPTS_PR.md) | `OR_PROC_ID` | high |
| [OR_CASE_APPTS_PS](OR_CASE_APPTS_PS.md) | `OR_PROC_ID` | high |
| [OR_LOG_ALL_PROC](OR_LOG_ALL_PROC.md) | `OR_PROC_ID` | high |

