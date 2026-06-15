# CLM_VALUES_REFERRAL_DX

> This table stores the referral diagnoses associated with the claim.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim value record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REFERRAL_DX` | VARCHAR |  | The diagnoses stated by the referring provider. |
| 4 | `REFERRAL_DX_QUAL` | VARCHAR |  | This code set for the diagnoses stated by the referring provider. |
| 5 | `REFERRAL_DX_CODE_SET_OID` | VARCHAR |  | The OID for the referral diagnosis code set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

