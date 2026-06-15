# OR_LNLG_PRESUR_EVT

> This table contains the Presurgery Event information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `PRE_SURG_EVENT_C_NAME` | VARCHAR | org | The pre-surgery event type. |
| 3 | `PRE_SURG_EVENT_DAT` | DATETIME |  | The date on which the pre-surgery event occurred. |
| 4 | `PRE_SURG_EVENT_TIM` | DATETIME (Local) |  | The time at which the pre-surgery event occurred. |
| 5 | `PRE_SURG_EVENT_LEN` | INTEGER |  | The length of the pre-surgery event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

