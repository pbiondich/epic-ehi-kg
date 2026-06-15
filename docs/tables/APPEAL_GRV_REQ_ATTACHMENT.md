# APPEAL_GRV_REQ_ATTACHMENT

> This table holds information about documents that are required to be attached to appeals and grievances. Each row corresponds to an individual document requirement and the document that satisfied the requirement.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TAT_TIME_STANDARD_C_NAME` | VARCHAR | org | The timeliness standard category ID that corresponds to this attachment requirement. |
| 4 | `DOC_INFO_TYPE_C_NAME` | VARCHAR | org | The attachment type category ID for this attachment requirement. |
| 5 | `ATTACHMENT_SUBMIT_UTC_DTTM` | DATETIME (UTC) |  | The date and time the required attachment was submitted. NULL indicates that the attachment is still outstanding. Stored in UTC. |
| 6 | `APPEAL_GRV_WKFL_STEP_C_NAME` | VARCHAR |  | The workflow step category ID that this attachment is required for. |
| 7 | `REQUIRED_FOR_TAT_YN` | VARCHAR |  | Indicates whether the attachment being attached resets the turnaround time clock. 'Y' indicates that attaching this attachment will reset the clock. 'N' or NULL indicates that attaching this attachment will not reset the clock. |
| 8 | `ATTACHMENT_SUBMIT_LOCAL_DTTM` | DATETIME (Local) |  | The date and time the required attachment was submitted. NULL indicates that the attachment is still outstanding. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

