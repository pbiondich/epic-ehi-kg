# CLP_EOB_CAS_LINE

> This table holds line-level claim adjustment reason code (CAS) data from the Explanation of Benefits (EOB) master file.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim print database record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EOB_CAS_LN_CVG_ID` | NUMERIC |  | The coverage record ID for the line-level explanation of benefits adjustment. |
| 4 | `EOB_CAS_CLM_LINE` | INTEGER |  | The service line number for the line-level explanation of benefits adjustment. |
| 5 | `EOB_LN_CAS_GRP_C_NAME` | VARCHAR | org | The line-level explanation of benefits adjustment group code. |
| 6 | `EOB_LN_CAS_RMT_CODE` | VARCHAR |  | The line-level explanation of benefits adjustment reason code. |
| 7 | `EOB_LN_CAS_AMT` | NUMERIC |  | The line-level explanation of benefits adjustment amount. |
| 8 | `EOB_LN_CAS_QTY` | INTEGER |  | The line-level explanation of benefits adjustment quantity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

