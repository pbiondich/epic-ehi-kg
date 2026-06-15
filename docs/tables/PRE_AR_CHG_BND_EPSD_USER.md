# PRE_AR_CHG_BND_EPSD_USER

> A table for the episode link user column for temporary accounts receivable (TAR). A record/charge line/episode line combination here corresponds to the same record/charge line/episode line combination in the other four bundled episode tables for TAR.

**Primary key:** `TAR_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the charge session record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `BND_EPSD_USER_ID` | VARCHAR |  | The user (background or person) who set the bundled episode |
| 5 | `BND_EPSD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

