# APPEAL_GRV_CHANGE_URGENCY

> Stores the change urgency requests for an appeal/grievance. Each row represents a change urgency request.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REQUESTED_URGENCY_C_NAME` | VARCHAR |  | The requested urgency category ID of the change urgency request. |
| 4 | `REQUEST_UTC_DTTM` | DATETIME (UTC) |  | The date and time in UTC that the change in urgency was requested. |
| 5 | `REQUEST_LOCAL_DTTM` | DATETIME (Local) |  | The date and time that the change in urgency was requested. |
| 6 | `INITIATED_BY_TYPE_C_NAME` | VARCHAR |  | The change urgency requested by type category ID for the change urgency request. |
| 7 | `URGENCY_COMMENTS` | VARCHAR |  | The comments entered on the change urgency request. |
| 8 | `URGENCY_DECISION_C_NAME` | VARCHAR |  | The change urgency decison category ID made on the urgency change request. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

