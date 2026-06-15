# OTP_DOSE_SUGG_OVRD

> This table contains all the Patient Order Template (OTP) items related to medication doses that are initially calculated by a dose suggestion programming point and are later overridden by a user.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 17  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The order template ID. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `PP_OVRD_RSN_C_NAME` | VARCHAR | org | Reason for entering a dose that is significantly different from the formula calculated dose. |
| 4 | `PP_OVRD_USER_ID` | VARCHAR |  | The user who is overriding the dose change warning. |
| 5 | `PP_OVRD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `PP_OVRD_DTTM` | DATETIME (Local) |  | The instant at which the dose change override reason was entered. |
| 7 | `PP_OVRD_AUTH_PR_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `FORM_DESC_AT_ORDER` | VARCHAR |  | The formula description at the time that the dose was entered. |
| 9 | `FORM_CALC_DOSE_AT_O` | NUMERIC |  | The dose that the formula suggested to the user at the time that the dose was entered. |
| 10 | `FORM_UNIT_AT_ORDR_C_NAME` | VARCHAR | org | The dose units that the formula suggested to the user at the time that the dose was entered. |
| 11 | `FORM_CALC_DESC_AT_O` | VARCHAR |  | The formula calculation description at the time the dose was entered. |
| 12 | `FORM_PARAM_INFO` | VARCHAR |  | The description of the formula parameters at the time the user entered the dose. |
| 13 | `ENTERED_DOSE` | VARCHAR |  | The dose that the user entered. |
| 14 | `ENTERED_DOSE_UNIT_C_NAME` | VARCHAR |  | The dose units that the user entered. |
| 15 | `OVRD_DOSE_DTTM` | DATETIME (Local) |  | The instant at which the override dose or override reason was entered or changed. |
| 16 | `FORMULA_DOSE_AT_SIGN` | VARCHAR |  | The signed dose of the order that was overridden. |
| 17 | `FORMULA_DOSE_UNIT_AT_SIGN_C_NAME` | VARCHAR |  | The signed dose unit of the order that was overridden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

