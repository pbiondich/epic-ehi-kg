# HNO_MYC_LET_INFO

> This table contains MyChart related information for letters. It includes whether a letter is released to MyChart and the date/time it was released to MyChart.

**Primary key:** `NOTE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `LET_REL_MYC_DTTM` | DATETIME (Local) |  | Instant at which the letter was released to MyChart. |
| 3 | `LET_REL_TO_MYC_YN` | VARCHAR |  | Indicates whether the letter is released to MyChart. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

