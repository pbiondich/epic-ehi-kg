# OTP_RX_DOSEHX_SEL

> This table extracts the related multiple response item Ingredient Dose Change Selection. The related tables are: OTP_RX_DOSEHX_TYPE OTP_RX_DOSEHX_DTTM OTP_RX_DOSEHX_USER OTP_RX_DOSEHX_DOSE OTP_RX_DOSEHX_UNIT OTP_RX_DOSEHX_RSN OTP_RX_DOSEHX_CMNT OTP_RX_DOSEHX_PCT

**Primary key:** `OTP_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient order template record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `IN_DOSE_CHG_SEL_C_NAME` | VARCHAR |  | The ingredient selection status on this value line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

