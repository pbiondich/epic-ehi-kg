# CL_PAT_EDU_TITLE

> Enterprise reporting table for patient education title and title status items.

**Primary key:** `PED_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The unique ID for the patient education record. |
| 2 | `LINE` | INTEGER | PK | Line count for the Patient education title data. |
| 3 | `PAT_TITLE_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 4 | `PAT_TITLE_STATUS_C_NAME` | VARCHAR |  | A category item that specifies each title's status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |

