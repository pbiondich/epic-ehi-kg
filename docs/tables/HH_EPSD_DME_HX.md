# HH_EPSD_DME_HX

> This table contains audit history for durable medical equipment (DMEs).

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HSPC_NONCVRD_RSN_C_NAME` | VARCHAR | org | Auditing history of the not-covered reasons for the DME. |
| 4 | `DME_TYPE_HX_NAME` | VARCHAR | org | Auditing history of the DME type. |
| 5 | `START_DATE` | DATETIME |  | Auditing history of the start of use dates for the DME. |
| 6 | `END_DATE` | DATETIME |  | Auditing history of the end of use dates for the DME. |
| 7 | `DME_COMMENTS_HX` | VARCHAR |  | Auditing history for the comments left about the DME. |
| 8 | `DME_DELETED` | INTEGER |  | Auditing history for whether the DME record is deleted. |
| 9 | `EDIT_USER` | VARCHAR |  | Auditing history for whether the DME record is deleted. |
| 10 | `EDIT_DTTM` | DATETIME (Attached) |  | Auditing history of the instant at which edits were made to data about the DME. |
| 11 | `EDIT_LINE` | INTEGER |  | Auditing history about which DME entry was edited. This is the line number found in column LINE of HH_EPSD_DME. |
| 12 | `HSPC_COVERED_C_NAME` | VARCHAR |  | Auditing history about the hospice coverage of the DME. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

