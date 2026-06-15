# REFERRAL_CE_CODE

> This audit table stores the Care Everywhere Codes.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_CODE_TYPE_C_NAME` | VARCHAR |  | Stores the type of the specialty code stored in column AUDIT_CODE. This column is used to audit data from incoming Care Everywhere referrals. |
| 4 | `AUDIT_CODE_RFNCID` | VARCHAR |  | Stores the reference ID corresponding to the specialty code stored in AUDIT_CODE. This reference ID is used as an index for the Diagnoses or Procedures table. This column is used to audit data from incoming Care Everywhere referrals. |
| 5 | `AUDIT_CODE` | VARCHAR |  | Stores the provider or department specialty code received from the referring organization with an external referral. The type of the specialty code is stored in column AUDIT_CODE_TYPE_C. This column is used to audit data from incoming Care Everywhere referrals. |
| 6 | `AUDIT_CODE_SYS` | VARCHAR |  | Stores the code system used by the referring organization to send the specialty code in column AUDIT_CODE. This column is used to audit data from incoming Care Everywhere referrals. |
| 7 | `AUDIT_CODE_NAME` | VARCHAR |  | Stores the name of the specialty code in column AUDIT_CODE. This column is used to audit data from incoming Care Everywhere referrals. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

