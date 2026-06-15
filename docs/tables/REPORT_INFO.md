# REPORT_INFO

> This table contains general information about report (HRX) records. Report records are created when users save options for various kinds of reports in Hyperspace, including application reports developed by Epic and Reporting Workbench reports created by Epic or users of your system. Among other things, this table includes information on the name, access, and search values of reports.

**Primary key:** `REPORT_INFO_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REPORT_INFO_ID` | NUMERIC | PK | The unique ID of the report record, not to be confused with the similarly-named REPORT_ID column, which is actually the ID of the template from which the report was created. |
| 2 | `REPORT_INFO_ID_REPORT_INFO_NAME` | VARCHAR |  | The name of the report. |
| 3 | `REPORT_INFO_NAME` | VARCHAR |  | The name of the report. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

