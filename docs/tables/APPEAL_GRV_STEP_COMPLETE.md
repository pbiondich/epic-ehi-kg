# APPEAL_GRV_STEP_COMPLETE

> This table contains information about when workflow steps were completed for a given appeal or grievance.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `APPEAL_GRV_WKFL_STEP_C_NAME` | VARCHAR |  | The category ID of the workflow step that was completed. |
| 4 | `COMPLETED_USER_ID` | VARCHAR |  | The unique ID of the user that completed the workflow step. If this workflow step was queued for completion and later auto-completed, this is the user that queued the completion. |
| 5 | `COMPLETED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `COMPLETED_UTC_DTTM` | DATETIME (UTC) |  | When the workflow step was completed (in UTC). If this workflow step was queued for completion and later auto-completed, this is when the user queued the completion. |
| 7 | `COMPLETED_LOCAL_DTTM` | DATETIME (Attached) |  | When the workflow step was completed (in local time). If this workflow step was queued for completion and later auto-completed, this is when the user queued the completion. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

