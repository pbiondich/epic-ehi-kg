# CLARITY_RPT

> This table contains the master file records for the Report Output Files (RPT) enterprise reporting reports. It is also used for configuration files for Report Template (HGR) records.

**Primary key:** `REPORT_ID`  
**Columns:** 3  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REPORT_ID` | NUMERIC | PK | The ID of the report record used in enterprise reporting web based system integration. |
| 2 | `REPORT_ID_REPORT_NAME` | VARCHAR |  | The name of the report |
| 3 | `REPORT_NAME` | VARCHAR |  | The name of the report |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [DP_COMM_ATTACHMENTS](DP_COMM_ATTACHMENTS.md) | `REPORT_ID` | high |
| [PAT_ENC_RPT_INFO](PAT_ENC_RPT_INFO.md) | `REPORT_ID` | high |
| [PAYOR_COMM_HX_REPORTS](PAYOR_COMM_HX_REPORTS.md) | `REPORT_ID` | high |

