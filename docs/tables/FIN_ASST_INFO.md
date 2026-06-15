# FIN_ASST_INFO

> This table contains financial assistance information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FIN_ASST_TRACKER_ID` | NUMERIC | FK→ | Stores the financial assistance tracker associated with the hospital account. |
| 4 | `FIN_ASST_EXCL_YN` | VARCHAR |  | Stores if the hospital account is not eligible for financial assistance. |
| 5 | `FIN_ASST_SOURCE_C_NAME` | VARCHAR |  | Stores the source of the financial assistance information on the hospital account. |
| 6 | `FIN_ASST_UPDATE_USER_ID` | VARCHAR |  | Stores the user who last updated the financial assistance tracker on the hospital account. |
| 7 | `FIN_ASST_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `FIN_ASST_UPDATE_DTTM` | DATETIME (UTC) |  | Stores the instant at which the user updated the financial assistance tracker on the hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_TRACKER_ID` | [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | name_stem | high |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

