# OR_CASE_INSTR_NEED

> The OR_CASE_INSTR_NEED table contains OR management system case surgical instruments.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the surgical instrument requested for the case. |
| 3 | `INSTRUMENT_PANEL` | VARCHAR |  | The panel where the surgical instrument is requested. |
| 4 | `INSTRUMENT_TYPE_C_NAME` | VARCHAR | org | The type of surgical instrument requested for the case. |
| 5 | `INSTRUMENT_CMT` | VARCHAR |  | A free-text comment about an instrument. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

