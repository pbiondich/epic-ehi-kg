# HH_EPSD_SURG_PROC_HX

> This table contains audit history for surgical procedures.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ICD_PROC_ID` | VARCHAR |  | Auditing history for surgical procedure IDs. |
| 4 | `ICD_PROC_ID_ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |
| 5 | `SURG_PROC_COMMENT_HX` | VARCHAR |  | Auditing history for comments on surgical procedures. |
| 6 | `SURG_PROC_HX_DATE` | DATETIME |  | Auditing history for the dates of surgical procedures. |
| 7 | `EDIT_USER_ID` | VARCHAR |  | Auditing history for the ID of the user who edited the surgical procedure data. |
| 8 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | Auditing history of the instant surgical procedure data was edited. |
| 10 | `EDIT_LINE` | INTEGER |  | Auditing history of the specific line number of the procedure that had its data edited. This is the line number found in column LINE of HH_EPSD_SURG_PROC_HX. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

