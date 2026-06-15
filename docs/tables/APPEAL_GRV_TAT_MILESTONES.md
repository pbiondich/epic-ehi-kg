# APPEAL_GRV_TAT_MILESTONES

> This table holds information about turnaround time milestones for appeals and grievances. Each row corresponds to an individual milestone and the date and time associated with the milestone.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TAT_TIME_STANDARD_C_NAME` | VARCHAR | org | The timeliness standard category ID that corresponds to this milestone. |
| 4 | `TAT_MILESTONE_C_NAME` | VARCHAR |  | The milestone type category ID for this milestone. |
| 5 | `TAT_MILE_INST_UTC_DTTM` | DATETIME (UTC) |  | The date and time associated with this milestone. Stored in UTC. |
| 6 | `TAT_MILE_DUE_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time associated with this milestone. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

