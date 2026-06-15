# DELINQUENCY_HISTORY

> The DELINQUENCY HISTORY table stores information about the history of delinquency on a premium billing account. It stores the new delinquency status, delinquency date, relevant invoice, workflow that set the information, and links to relevant records.

**Primary key:** `PB_ACCT_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACCT_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DLQ_HX_INST_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant that the delinquency information changed. |
| 4 | `DLQ_HX_UPD_ACCT_DQ_STS_C_NAME` | VARCHAR | org | The Delinquency Status category ID for the premium billing account. |
| 5 | `DLQ_HX_LAST_PB_INVC_ID` | VARCHAR |  | The unique ID of the delinquency history premium billing invoice. |
| 6 | `DLQ_HX_EPSD_DATE` | DATETIME |  | The date of the premium billing accounts delinquency episode began. |
| 7 | `DLQ_HX_USER_ID` | VARCHAR |  | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 8 | `DLQ_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `DLQ_HX_WORKFLOW_C_NAME` | VARCHAR |  | The Delinquency History - Workflow category ID for the premium billing account. |
| 10 | `DLQ_HX_EVENT_ID` | VARCHAR |  | The unique ID of the event that caused a change in delinquency information. |
| 11 | `DLQ_HX_EVENT_ID_EVENT_NAME` | VARCHAR |  | The name of the event. |
| 12 | `DLQ_HX_PAYMENT_ID` | VARCHAR |  | The unique ID of the payment associated with the change in deliquency information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |

