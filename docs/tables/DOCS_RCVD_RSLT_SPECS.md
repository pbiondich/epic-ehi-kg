# DOCS_RCVD_RSLT_SPECS

> This table stores discrete specimen information received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier for the received Document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `SPEC_ORDER_REFID` | VARCHAR |  | Unique identifier for result; ties multiple specimens to one result |
| 6 | `SPEC_REFID` | VARCHAR |  | Unique identifier for this specimen, which ties it to codes stored in Mapping Information (SI DXR 7000). |
| 7 | `SPEC_EXTID` | VARCHAR |  | External ID for specimen; may not be unique. |
| 8 | `SPEC_TYPE_NAME` | VARCHAR |  | String name of specimen type. |
| 9 | `SPEC_TYPE_C_NAME` | VARCHAR | org | The Category ID for the specimen type (I ORD 300) |
| 10 | `SPEC_SOURCE_NAME` | VARCHAR |  | The free text name of the specimen source. |
| 11 | `SPEC_SOURCE_C_NAME` | VARCHAR | org | The Category ID for the specimen source, from Specimen Source ID (I ORD 325). |
| 12 | `SPEC_BULK_INCL_DATE` | DATETIME |  | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |
| 13 | `SPEC_BULK_STAT_C_NAME` | VARCHAR |  | The status of this data element within DINE. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

