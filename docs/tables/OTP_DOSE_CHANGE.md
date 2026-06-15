# OTP_DOSE_CHANGE

> The dose change history for an order template.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The order template ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to a dose change of the order template in this record. |
| 3 | `DOSE_CHANGE_TYP_C_NAME` | VARCHAR | org | The type of dose change made to the order template in this record, such as Initial Dose, Order Composer, Dose Modification, or Change Propagation. |
| 4 | `DOSE_CHANGE_INST` | DATETIME (Local) |  | The date/time in external format when a dose of the order template in this record was changed. |
| 5 | `DOSE_CHANGE_USER_ID` | VARCHAR |  | The user ID of the person who made the dose change to the order template in this row. |
| 6 | `DOSE_CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `DOSE_CHANGE_AMT` | VARCHAR |  | The new dose of the order template in this row. |
| 8 | `DOSE_CHANGE_UNIT_C_NAME` | VARCHAR | org | The dose unit for the new dose of the order template in this row. |
| 9 | `DOSE_CHANGE_RSN_C_NAME` | VARCHAR | org | The reason for the dose change to the order template in this row. |
| 10 | `DOSE_CHANGE_COMMENT` | VARCHAR |  | User free text comment on the reason for the dose change to the order template in this row. |
| 11 | `DOSE_CHANGE_PCT` | NUMERIC |  | The percentage change (positive or negative) made to the dose of the order template in this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

