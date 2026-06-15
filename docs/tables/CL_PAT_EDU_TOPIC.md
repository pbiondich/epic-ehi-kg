# CL_PAT_EDU_TOPIC

> Enterprise reporting table for patient topic items.

**Primary key:** `PED_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The Unique ID for the Patient Education Record. |
| 2 | `LINE` | INTEGER | PK | Line count for the Patient education topic data. |
| 3 | `PAT_TOPIC_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 4 | `PAT_TOPIC_TITLE_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 5 | `PAT_TOPIC_STATUS_C_NAME` | VARCHAR |  | A category item that specifies each topic's status. |
| 6 | `PAT_TOPIC_KEY` | VARCHAR |  | The education topic key for patient education record. This is a string of Title^Topic |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |

