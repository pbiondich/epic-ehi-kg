# COVERAGE_NOTE_INFO

> This table contains information about notes attached to coverage records.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTE_ID` | VARCHAR | shared | The unique identifier of the note associated with the coverage. |
| 4 | `NOTE_DATE` | DATETIME |  | The date the note was created. |
| 5 | `NOTE_DTTM` | DATETIME (Local) |  | The date and time the note was created. |
| 6 | `NOTE_USER_ID` | VARCHAR |  | The user who created the note. |
| 7 | `NOTE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

