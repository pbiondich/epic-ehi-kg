# IP_SNAPSHOT_SUM

> Order summary at time of discharge snapshot.

**Primary key:** `EVENT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique identifier for the event record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated order in the event record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple lines used to store the summary of instructions for the order record. |
| 4 | `SNAPSHOT_LNG_SUMMAR` | VARCHAR |  | A summary of the instructions in the order record at the time a patient was discharged or when a summary of the patient's visit, including follow-ups and instructions for what medications to take at home, was printed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

