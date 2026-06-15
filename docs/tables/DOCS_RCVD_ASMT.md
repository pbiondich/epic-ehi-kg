# DOCS_RCVD_ASMT

> Table to maintain information related to assessments and risk scores. The information stored in this table was received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ASMT_REF_ID` | VARCHAR |  | This item stores the unique reference identifier associated with the assessment. |
| 6 | `ASMT_SRC_DXR` | NUMERIC |  | The Contact Serial Number (CSN) of the received document record from which the assessment for this row was sourced. |
| 7 | `ASMT_VAL` | INTEGER |  | Value associated with this assessment. |
| 8 | `ASMT_UNIT` | VARCHAR |  | Unit associated with this assessment. |
| 9 | `ASMT_DATETIME` | DATETIME (Local) |  | The clinically relevant date for this assessment. This could be the recorded date or the date of an update for a current assessment. |
| 10 | `ASMT_LAST_UPD_INST_DTTM` | DATETIME (UTC) |  | This item stores the last update instant of this assessment in UTC. |
| 11 | `ASMT_NAME` | VARCHAR |  | This item stores the assessment name sent by the external source. |
| 12 | `ASMT_STATUS_C_NAME` | VARCHAR |  | The ASMT_STATUS_C column contains the status of a received assessment. Under normal circumstances, only cancelled or removed statuses will be filled out. |
| 13 | `ASMT_EXT_DATA_FILTER_REASON_C_NAME` | VARCHAR |  | Stores the reason why an external assessment was filtered from the composite record (I DXR 14712) |
| 14 | `ASMT_BULK_STAT_C_NAME` | VARCHAR |  | The status of this data element within DINE. |
| 15 | `ASMT_BULK_INCL_DATE` | DATETIME |  | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

