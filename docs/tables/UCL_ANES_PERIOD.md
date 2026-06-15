# UCL_ANES_PERIOD

> The UCL_ANES_PERIOD table contains information about the period included for the anesthesia procedure.

**Primary key:** `UCL_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK FK→ | The unique ID associated with the charge record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANES_PRD_ST_DT_TM` | DATETIME (Local) |  | The start date and time of the anesthesia procedure. |
| 4 | `ANES_PRD_ED_DT_TM` | DATETIME (Local) |  | The end date and time of the anesthesia procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `UCL_ID` | [CLARITY_UCL](CLARITY_UCL.md) | sole_pk | high |

