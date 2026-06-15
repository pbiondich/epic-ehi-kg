# OTP_DOSE_PARAMS

> The dosing parameters for the order template.

**Primary key:** `OTP_ID`  
**Columns:** 16  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The order template ID. |
| 2 | `OTP_DW_RECORD_INST` | DATETIME (Local) |  | The date/time in external format when the dosing weight was recorded for the order template in this row. |
| 3 | `OTP_WT_SOURCE_C_NAME` | VARCHAR | org | The source of the dosing weight recorded for the order template in this row. |
| 4 | `OTP_WT_COMMENTS` | VARCHAR |  | The comments for the dosing weight recorded for the order template in this row. |
| 5 | `OTP_DOSING_HEIGHT` | NUMERIC |  | The dosing height in inches for the order template in this row |
| 6 | `OTP_HT_REC_INST` | DATETIME (Local) |  | The date/time in external format when the dosing height was recorded for the order template in this row. |
| 7 | `OTP_HT_SOURCE_C_NAME` | VARCHAR | org | The source of the dosing height recorded for the order template in this row. |
| 8 | `OTP_HT_COMMENTS` | VARCHAR |  | The comments for the dosing height recorded for the order template in this row. |
| 9 | `OTP_DOSING_BSA` | NUMERIC |  | The dosing body surface area (BSA) for the order template in this row. |
| 10 | `OTP_BSA_SRC_C_NAME` | VARCHAR | org | The source of the dosing BSA for the order template in this row. |
| 11 | `OTP_BSA_CALC_DETAIL` | VARCHAR |  | The dosing BSA calculation details for the order template in this row. |
| 12 | `OTP_BSA_COMMENTS` | VARCHAR |  | The dosing BSA comments recorded for the order template in this row. |
| 13 | `OTP_DOSING_WEIGHT` | NUMERIC |  | Stores order-specific dosing weight in kg. |
| 14 | `OTP_DOSING_BSA_ORIGINAL` | NUMERIC |  | The original (uncapped) BSA of an order |
| 15 | `RECENT_RULE_DAT` | NUMERIC |  | If this medication has a dosing rule, this will be the contact date (DAT) of the most recent dosing rule that was checked and matched the patient. |
| 16 | `PAT_REPORTED_WEIGHT_SOURCE_C_NAME` | VARCHAR |  | Indicates the source of a patient-reported dosing weight value, such as reported by a smart device or manually entered by the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

