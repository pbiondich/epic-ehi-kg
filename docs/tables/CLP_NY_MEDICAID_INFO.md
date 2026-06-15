# CLP_NY_MEDICAID_INFO

> This table contains information about data that will be used when processing claims on the eMedNY 150003 paper claim form for New York Medicaid.

**Primary key:** `CLAIM_PRINT_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `EMEDNY_PAYMENT_SOURCE_MCARE_C_NAME` | VARCHAR |  | This is the single-digit source code indicator that indicates Medicare's involvement in paying for these charges on the eMedNY 150003 claim form. |
| 3 | `EMEDNY_PAYMENT_SOURCE_OTHER_C_NAME` | VARCHAR |  | This is a single-digit code indicating whether the patient has a coverage besides Medicare and Medicaid on the eMedNY 150003 claim form. |
| 4 | `EMEDNY_PAYMENT_SOURCE_INS_CODE` | VARCHAR |  | This is the two-digit insurance code for the commercial coverage, if any, on the eMedNY 150003 claim form. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

