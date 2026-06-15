# LCI_HISTORICAL_DATA

> Data describing the beneficiary's coverage over time.

**Primary key:** `EXTERNAL_CVG_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EXTERNAL_CVG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the external coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HIST_FILE_TIMESTAMP_UTC_DTTM` | DATETIME (UTC) |  | Contains the file timestamp for every file loaded. |
| 4 | `HIST_EXTERNAL_COVERAGE_TYPE_C_NAME` | NUMERIC |  | The coverage type. This data is tracked over time per file. |
| 5 | `HIST_COVERAGE_BEGIN_DATE` | DATETIME |  | The effective start date for the coverage. This data is tracked over time per file. |
| 6 | `HIST_MEDICARE_STATUS_C_NAME` | NUMERIC |  | The reason for the beneficiary's Medicare entitlement. This data is tracked over time per file. |
| 7 | `HIST_MCARE_MCAID_DUAL_STAT_C_NAME` | NUMERIC |  | This field indicates whether the patient has Medicare, Medicaid, both, neither, or some partial combination. This data is tracked over time per file. |
| 8 | `HIST_ORIGINAL_MCARE_ELIG_RSN_C_NAME` | NUMERIC | org | The original reason for the beneficiary's Medicare entitlement. This data is tracked over time per file. |
| 9 | `HIST_ENTITLEMENT_BUYIN_IND_C_NAME` | NUMERIC |  | Medicare coverage type (Part A, B, or both) and whether the state paid premiums through a buy-in program. This data is tracked over time per file. |
| 10 | `HIST_HOSPICE_BEGIN_DATE` | DATETIME |  | The date that Hospice care enrollment begins. This data is tracked over time per file. |
| 11 | `HIST_HOSPICE_END_DATE` | DATETIME |  | The date that Hospice care enrollment ends. This data is tracked over time per file. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

