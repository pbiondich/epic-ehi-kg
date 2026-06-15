# ACCUM_INSTANCE_DATES

> Dates accumulated on the associated accumulation line.

**Primary key:** `ACCUMULATION_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCUMULATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the accumulation record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the accumulation line associated with this accumulation. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple dates associated with a specific accumulation line within this accmulation. |
| 4 | `ACCUM_INSTANCE_DATE` | DATETIME |  | The dates that were accumulated on this accumulation line |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

