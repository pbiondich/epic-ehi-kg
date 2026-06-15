# TODO_ENRLL_NOTIF_LOG

> This table contains information regarding the first ad hoc task notifications that were sent.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ENRLL_NOTIF_UTC_DTTM` | DATETIME (UTC) |  | The timestamp in UTC instant when the To Do enrollment notification was sent. |
| 4 | `NOTIF_TODO_SEND_MTHD_C` | VARCHAR |  | The send method of the To Do enrollment notification sent. |
| 5 | `NOTIF_RECIP_MYPT_ID` | VARCHAR |  | WPR ID of the recipient of the To Do enrollment notification. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

