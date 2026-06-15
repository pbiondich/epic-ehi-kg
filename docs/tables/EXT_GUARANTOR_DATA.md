# EXT_GUARANTOR_DATA

> Clarity table for External Guarantor data.

**Primary key:** `EXTERNAL_CVG_ID`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EXTERNAL_CVG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the external coverage record record. |
| 2 | `ASSOCIATED_ACCT_ID` | NUMERIC |  | The guarantor record associated with this External Guarantor data. This is the guarantor record linked or created from this External Guarantor data. |
| 3 | `EXT_GUAR_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The Contact Serial Number associated with this External Guarantor record. |
| 4 | `EXT_GUAR_NAME` | VARCHAR |  | The name of the guarantor that this External Guarantor record represents. |
| 5 | `EXT_GUAR_DOB_DATE` | DATETIME |  | The date of birth for the guarantor that this External Guarantor record represents. |
| 6 | `EXT_GUAR_MOBILE` | VARCHAR |  | The mobile phone number of the guarantor that this External Guarantor record represents. |
| 7 | `EXT_GUAR_EMAIL` | VARCHAR |  | The email address of the guarantor that this External Guarantor record represents. |
| 8 | `EXT_GUAR_REL_TO_PAT_C_NAME` | VARCHAR | org | The relationship to patient category value of the guarantor that this External Guarantor record represents. |
| 9 | `EXT_GUAR_ACCT_TYPE_2_C_NAME` | VARCHAR | org | The account type category value of the guarantor that this External Guarantor record represents. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EXT_GUAR_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

