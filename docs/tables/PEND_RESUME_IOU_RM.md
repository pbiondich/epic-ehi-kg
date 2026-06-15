# PEND_RESUME_IOU_RM

> This table extracts the related multiple response Pend - Resume Indications of Use (I IEV 2090) item, which records the indications of use for pended medications in medication reconciliation

**Primary key:** `EVENT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique ID for the event record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with pended indications associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of multiple values associated with a specific group of data within this record. |
| 4 | `PEND_INDICATIONS_ID` | NUMERIC |  | This column saves the pended indications when a discharge med is resumed. |
| 5 | `PEND_INDICATIONS_ID_MEDICAL_COND_NAME` | VARCHAR |  | This contains the name of the medical condition. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

