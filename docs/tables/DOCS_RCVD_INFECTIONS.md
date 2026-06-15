# DOCS_RCVD_INFECTIONS

> This table stores patient infection information received from external sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `INFECTION_REFERENCE_ID` | VARCHAR |  | The unique reference identifier associated with the infection. |
| 6 | `INFECTION_NAME` | VARCHAR |  | The name of the infection. |
| 7 | `INFECTION_TYPE_C_NAME` | VARCHAR | org | The type of the infection. |
| 8 | `INFECTION_RECEIVED_STATUS_C_NAME` | VARCHAR |  | The HL7 Act status received for the infection. |
| 9 | `INFECTION_START_DATE` | DATETIME (Local) |  | The date the infection started. |
| 10 | `INFECTION_END_DATE` | DATETIME (Local) |  | The date the infection was marked resolved. |
| 11 | `INFECTION_SRC_DXR_CSN` | NUMERIC |  | The contact serial number of the DXR record that owns the instance of this infection. |
| 12 | `INFECTION_LAST_UPD_INST_DTTM` | DATETIME (UTC) |  | Stores the last time the infection has been updated. |
| 13 | `INFECTION_HIST_STATUS_C_NAME` | VARCHAR |  | Indicates whether the infection is currently active or historical. |
| 14 | `INFECTION_LAST_INDICATED_DATE` | DATETIME |  | This item stores the most recent date on which the infection was indicated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

