# OR_LOG_METRIC_DETAILS

> Stores details for log based metrics that respect Epic standard definitions. The values for each log in this table correspond to the values contributing to the numerator and denominator values in OpTime Cogito Summarized Facts (CSF) metrics. Note that the values associated to each log for these metrics may differ from those values found on other tables like OR_LOG_VIRTUAL as it is possible these metrics respect different settings than those at your organization.

**Primary key:** `LOG_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the log record. |
| 2 | `EPIC_D2B_ADMISSION_DATE` | DATETIME |  | The patient's admission date associated with the log. |
| 3 | `EPIC_TOTAL_D2B_TIME` | INTEGER |  | Total time (in seconds) that was calculated for a STEMIs door to balloon time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

