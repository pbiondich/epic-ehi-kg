# UCL_ANES_EXCLUSION

> The UCL_ANES_EXCLUSION table contains information about the period excluded from the anesthesia procedure.

**Primary key:** `UCL_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK FK→ | The unique ID associated with the charge record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANES_EXCL_ST_DT_TM` | DATETIME (Local) |  | The starting date and time of the period exclusion for the anesthesia. |
| 4 | `ANES_EXCL_ED_DT_TM` | DATETIME (Local) |  | The end date and time of the period exclusion for the anesthesia. |
| 5 | `ANES_EXCL_COMMENT` | VARCHAR |  | The comment of the period exclusion for the anesthesia. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `UCL_ID` | [CLARITY_UCL](CLARITY_UCL.md) | sole_pk | high |

