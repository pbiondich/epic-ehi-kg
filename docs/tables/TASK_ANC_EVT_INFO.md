# TASK_ANC_EVT_INFO

> This table contains filing information of the anchor event linked to the task.

**Primary key:** `TASK_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TASK_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANC_EVT_FILE_DATE` | DATETIME |  | The date in local time that this anchor event action occurs. |
| 4 | `ANC_EVT_ENC_CSN_ID` | NUMERIC | FK→ | The CSN of the encounter that is associated with this anchor event action. |
| 5 | `ANC_EVT_DATE` | DATETIME |  | The date in local time of the event that is associated with this anchor event action. |
| 6 | `ANC_EVT_FILE_UTC_DTTM` | DATETIME (UTC) |  | The instant in UTC time on which this anchor event action occurs. |
| 7 | `ANC_EVT_ACTION_C_NAME` | VARCHAR |  | The anchor event action that occurrs. |
| 8 | `ANC_EVT_UTC_DTTM` | DATETIME (UTC) |  | The instant in UTC of the event that is associated with this anchor event action. |
| 9 | `ANC_EVT_LPP_ID` | NUMERIC |  | The anchor event extension that was used for the anchoring or the unanchoring actions. |
| 10 | `ANC_EVT_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANC_EVT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

