# CLM_CVG_INFO

> This table stores claim level coverage related information.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the Claim Info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ALL_CVG_ID` | NUMERIC |  | Stores coverage ID. |
| 4 | `AUTH_NUM` | VARCHAR |  | Stores the authorization number for the corresponding coverage. |
| 5 | `AUTH_TYP_C_NAME` | VARCHAR |  | Store the authorization type for the corresponding coverage. |
| 6 | `AUTH_SOURCE_REFERRAL_ID` | NUMERIC |  | The unique ID of the referral or auth/cert record when the authorization number on the row was found in the referral or auth/cert. |
| 7 | `AUTH_SOURCE_AUTH_ID` | NUMERIC |  | The unique ID of the service level authorization record when the authorization number on the row was found in the authorization record. |
| 8 | `AUTH_SOURCE_HSP_ACCOUNT_ID` | NUMERIC |  | The unique ID of the hospital account when the authorization number on the row was found in the account. |
| 9 | `AUTH_SOURCE_CLAIM_ID` | NUMERIC |  | The unique ID of the hospital account when the authorization number on the row was found in the account. |
| 10 | `AUTH_NUM_SOURCE_C_NAME` | VARCHAR |  | The auth number search precedence category ID identifying where the authorization number was found. |
| 11 | `AUTH_PB_RFL_RECORD_SOURCE_C_NAME` | VARCHAR |  | The Professional Billing referral source search precedence category ID identifying where the source referral or auth/cert record was found. |
| 12 | `AUTH_HB_RFL_RECORD_SOURCE_C_NAME` | VARCHAR |  | The Hospital Billing referral source search precedence category ID identifying where the source referral or auth/cert record was found. |
| 13 | `AUTH_SOURCE_TREATMENT_PLAN_ID` | VARCHAR |  | The unique ID of the dental treatment plan record when the authorization number on the row was found in the treatment plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

