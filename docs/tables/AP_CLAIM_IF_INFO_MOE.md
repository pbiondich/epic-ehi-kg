# AP_CLAIM_IF_INFO_MOE

> Claim level data that can be sent or received by prospective payment systems (PPS) pricers that use the Medicaid Outpatient Editor (MOE).

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MOE_RELEASE_VERSION` | VARCHAR |  | Editor release version number applicable to this claim. |
| 4 | `MOE_CLM_ERROR_NUM` | VARCHAR |  | Number of claim-level edits returned. |
| 5 | `MOE_DX_ERROR_NUM` | VARCHAR |  | Number of diagnosis edits returned. |
| 6 | `MOE_PX_ERROR_NUM` | VARCHAR |  | Number of procedure edits returned. |
| 7 | `MOE_TOTAL_ERRORS` | VARCHAR |  | Total number of edits identified for this claim. |
| 8 | `MOE_CLM_DISPOSITION` | VARCHAR |  | Overall disposition of the claim, including claim-level, diagnosis, and procedure edits. |
| 9 | `MOE_ERROR_DISP` | VARCHAR |  | Claim disposition flag array; one flag for each disposition. |
| 10 | `MOE_HI_CLM_ERR_DISP` | VARCHAR |  | Highest claim-level edit disposition. |
| 11 | `MOE_CLM_ERRORS` | VARCHAR |  | Codes that describe any claim-level edits found by the editor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

