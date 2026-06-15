# WEB_VIEW_INFO

> The WEB_VIEW_INFO table contains information about which users are viewing patient summary extract (LNO) reports from the Web. Data in this table includes the user's id, the user's submitter id, and the exact time the user viewed the report. Each row in this table represents a time that a user has viewed the particular report.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the extract record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WEB_VIEWER_EMP_ID` | VARCHAR |  | Keep track of which users (EMP ID) have viewed the Patient Summary Extracts (LNO) from Web Outreach. |
| 4 | `WEB_VIEWER_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `WEB_VIEWER_SMT_ID` | NUMERIC |  | Keep track of the submitter (SMT ID) of the user viewing the Patient Summary Extracts (LNO) from Web Outreach. |
| 6 | `WEB_VIEWER_SMT_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 7 | `WEB_VIEW_DTTM` | DATETIME (Local) |  | Keep track of when the Patient Summary Extracts (LNO) was viewed from the Web. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

