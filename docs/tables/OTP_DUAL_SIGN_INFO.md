# OTP_DUAL_SIGN_INFO

> The dual sign history for an order template.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The order template ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to each signing of the order template in this row. |
| 3 | `HX_DUALSIGN_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `HX_DUALSIGN_INST` | DATETIME (Local) |  | The date/time in external format of a signing of the order template in this row. |
| 5 | `DUAL_SIGN_CNXT_HX_C_NAME` | VARCHAR | org | The context of revalidation of a signing of the order template in this row. |
| 6 | `DUAL_SIGN_WKS_HX_ID_WORKSTATION_NAME` | VARCHAR |  | This is the internal workstation name. |
| 7 | `DUAL_SIGN_RSLT_HX_C_NAME` | VARCHAR |  | The result of validation for a signing of the order template in this row. |
| 8 | `DUAL_SIGN_DEVC_HX_C_NAME` | VARCHAR | org | The signing device for a signing of the order template in this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

