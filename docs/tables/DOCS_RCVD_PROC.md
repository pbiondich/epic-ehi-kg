# DOCS_RCVD_PROC

> This table stores procedure information received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PROC_REF_ID` | VARCHAR |  | This item stores the unique reference ID. |
| 6 | `PROC_TYPE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 7 | `PROC_TYPE_TXT` | VARCHAR |  | This item stores the free text name for the external procedure. |
| 8 | `PROC_PERF_AT_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 9 | `PROC_PERF_AT_TXT` | VARCHAR |  | This item stores the free text location where the external procedure was performed. |
| 10 | `PROC_START_DATE` | DATETIME |  | This item stores the start date of the external procedure. |
| 11 | `PROC_END_DATE` | DATETIME |  | This item stores the end date of the external procedure. |
| 12 | `PROC_EVENT_ID` | VARCHAR |  | This item holds the event identifier of the event information for the procedure. |
| 13 | `PROC_MASTER_REF_ID` | VARCHAR |  | This item will be used to indicate duplicate procedure data. |
| 14 | `PROC_LST_UPD_INST_DTTM` | DATETIME (UTC) |  | Stores the last update instant of the procedure in Coordinated Universal Time (UTC). |
| 15 | `PROC_UNSUCCESSFUL_FLG_C_NAME` | VARCHAR |  | Indicates whether a procedure was an unsuccessful attempt |
| 16 | `PROC_UNSUCCESS_INST_UTC_DTTM` | DATETIME (UTC) |  | Instant the procedure unsuccessful flag was set |
| 17 | `PROC_STATE_C_NAME` | VARCHAR |  | This item contains the status code of a procedure when received from a document. |
| 18 | `PROC_DUP_INT_PROC_ID` | NUMERIC |  | Stores the ID of the Order record of an internal charge that is a duplicate of this row in an external document record. |
| 19 | `PROC_DUP_INT_UCL_ID` | VARCHAR |  | Stores the ID of the Universal Charge Lines record of an internal charge that is a duplicate of this row in an external document record. |
| 20 | `PROC_DUP_INT_TX_ID` | NUMERIC |  | Stores the ID of the Accounts Receivable Transaction record of an internal charge that is a duplicate of this row in an external document record. |
| 21 | `PROC_DUP_INT_HOSP_TX_ID` | NUMERIC |  | Stores the ID of the Hospital Permanent Transaction record of an internal charge that is a duplicate of this row in an external document record. |
| 22 | `PROC_FILTER_RSN_C_NAME` | VARCHAR |  | Stores the reason why an external procedure should be filtered from the composite record |
| 23 | `EXT_PROC_BULK_STAT_C_NAME` | VARCHAR |  | The status of this data element within DINE. |
| 24 | `PROC_BULK_INCL_DATE` | DATETIME |  | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

