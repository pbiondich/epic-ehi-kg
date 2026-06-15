# OR_LOG_VERIF

> The OR_LOG_VERIF table contains OR management system log verification information.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log the log verification refers to |
| 2 | `LINE` | INTEGER | PK | The number of the line of the log verification in the surgical log. |
| 3 | `VERIF_STAFF_ID` | VARCHAR |  | The ID of the staff member who verified the log. |
| 4 | `VERIF_STAFF_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `VERIFICATION_DATE` | DATETIME (Local) |  | The date on which the log was verified. |
| 6 | `OR_VERIFY_TYPE_C_NAME` | VARCHAR | org | The type of verification performed. |
| 7 | `VERIFY_ANSWER_ID` | VARCHAR |  | The answer (HQA) record for the verification. |
| 8 | `ATTEST_FLT_ID` | VARCHAR |  | Holds the flowsheet template (FLT) ID used for documenting flowsheet information for the current attestation. |
| 9 | `ATTEST_FLT_ID_DISPLAY_NAME` | VARCHAR |  | The display name associated with this template. |
| 10 | `ATTEST_FLOWSHT_INST` | DATETIME (Local) |  | Holds the flowsheet instant at which the flowsheet documentation is stored for the current attestation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

