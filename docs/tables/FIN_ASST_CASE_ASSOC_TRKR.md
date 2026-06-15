# FIN_ASST_CASE_ASSOC_TRKR

> This table contains information on how financial assistance program trackers are linked to each other in a financial assistance case.

**Primary key:** `FIN_ASST_CASE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier for the financial assistance case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FIN_ASST_PROGRAM_ID` | NUMERIC | FK→ | This item stores the financial assistance program for the associated trackers. |
| 4 | `FIN_ASST_PROGRAM_ID_PROGRAM_NAME` | VARCHAR |  | The name of the financial assistance program record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |
| `FIN_ASST_PROGRAM_ID` | [FIN_ASST_PROGRAM](FIN_ASST_PROGRAM.md) | sole_pk | high |

