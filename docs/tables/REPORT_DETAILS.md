# REPORT_DETAILS

> This table contains information about general characteristics of reports containing print groups. This table includes whether it is an HTML report or time sensitive, the stylesheet used, setup extensions, print class, and content type.

**Primary key:** `LRP_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LRP_ID` | VARCHAR | PK | The unique ID of the report. |
| 2 | `LRP_ID_REPORT_NAME` | VARCHAR |  | The name of the report |
| 3 | `REPORT_NAME` | VARCHAR |  | The name of the report |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [DP_COMM_LRP_RM](DP_COMM_LRP_RM.md) | `LRP_ID` | high |
| [PAYOR_COMM_HX](PAYOR_COMM_HX.md) | `LRP_ID` | high |

