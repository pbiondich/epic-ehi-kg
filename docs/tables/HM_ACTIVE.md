# HM_ACTIVE

> This table contains information regarding potential future Health Maintenance completions.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HM_ACT_STD_TOPIC_ID` | NUMERIC |  | This column stores a Health Maintenance Topic ID for potential future completions. |
| 4 | `HM_ACT_STD_TOPIC_ID_NAME` | VARCHAR |  | The name of the health maintenance topic. |
| 5 | `HM_ACT_DATE` | DATETIME |  | This column displays the date of action for a potential Health Maintenance completion. |
| 6 | `HM_ACT_ORDER_ID` | NUMERIC |  | This column displays the orders that, once completed, will complete a Health Maintenance topic. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

