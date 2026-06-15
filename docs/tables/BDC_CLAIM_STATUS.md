# BDC_CLAIM_STATUS

> This table contains information about the claim status for claim status follow-up (BDC) records, including claim status reason codes and claim status codes.

**Primary key:** `BDC_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the den/corr rec record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLAIM_STAT_RSN_C_NAME` | VARCHAR |  | Status reason code of the claim status message linked to the claim status follow-up record. |
| 4 | `CLM_STATUS_CODE_C_NAME` | VARCHAR | org | Status code loaded from a ANSI 277 message from the payer that indicates the status of the claim. |
| 5 | `CLM_STATUS_DATA` | VARCHAR |  | Status code string for when the status code is unmapped. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

