# CAREPLAN_PROG_NOTE

> This table contains information about the list of progress notes filed from Care Plans activity for each Care Plan record.

**Primary key:** `CARE_INTG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CARE_INTG_ID` | VARCHAR | PK FK→ | The unique identifier for the careplan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CP_PROG_NOTES_ID` | VARCHAR |  | The unique ID of the Progress Note (HNO) that was filed from the Care Plans activity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CARE_INTG_ID` | [CAREPLAN_INFO](CAREPLAN_INFO.md) | sole_pk | high |

