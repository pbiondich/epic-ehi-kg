# OTP_SIGN_INFO

> The signing history for an order template.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The order template ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to each signing of the order template in this row. |
| 3 | `OTP_PREAUTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `OTP_PREAUTH_HX_TM` | DATETIME (Local) |  | The date/time in external format of a signing of the order template in this row. |
| 5 | `ORD_SIGN_CNTXT_HX_C_NAME` | VARCHAR | org | The context of revalidation of a signing of the order template in this row. |
| 6 | `ORD_SIGN_WKS_HX_ID_WORKSTATION_NAME` | VARCHAR |  | This is the internal workstation name. |
| 7 | `ORD_SIGN_RSLT_HX_C_NAME` | VARCHAR |  | The result of validation of a signing of the order template in this row. |
| 8 | `ORD_SIGN_DEVCE_HX_C_NAME` | VARCHAR | org | The device used for a signing of the order template in this row. |
| 9 | `OTP_SIGN_HX_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the history of the patient CSN that the order template was signed in. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |
| `OTP_SIGN_HX_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

