# CLP_EOB_CAS_CLM

> This table contains claim-level Claim Adjustment Segment (CAS) data for non-primary claims.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim print database record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EOB_CAS_CLM_CVG_ID` | NUMERIC |  | The coverage record ID for the claim-level explanation of benefits adjustment. |
| 4 | `EOB_CLM_CAS_GRP_C_NAME` | VARCHAR | org | The claim-level explanation of benefits adjustment group code. |
| 5 | `EOB_CLM_CAS_RMT_CD` | VARCHAR |  | The claim-level explanation of benefits adjustment reason code. |
| 6 | `EOB_CLM_CAS_AMT` | NUMERIC |  | The claim-level explanation of benefits adjustment amount. |
| 7 | `EOB_CLM_CAS_QTY` | INTEGER |  | The claim-level explanation of benefits adjustment quantity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

