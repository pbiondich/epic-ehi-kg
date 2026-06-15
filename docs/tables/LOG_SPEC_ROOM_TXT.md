# LOG_SPEC_ROOM_TXT

> This table contains any free text comments about room special needs in the log record.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ROOM_FREETEXT` | VARCHAR |  | Used to document free text special table requests. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

