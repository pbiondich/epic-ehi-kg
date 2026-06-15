# LETTER_PRINT_HISTORY

> Table for per claim EOB print data.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LETTER_HX_NOTIF_PRINT_TYPE_C_NAME` | VARCHAR |  | The print type of the letter |
| 4 | `LETTER_HX_DTTM` | DATETIME (Attached) |  | The print instant of the letter |
| 5 | `LETTER_HX_USER_ID` | VARCHAR |  | The user who printed the letter |
| 6 | `LETTER_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `LETTER_HX_PRINT_JOB_CLASS_C_NAME` | VARCHAR |  | The letter type of the letter |
| 8 | `LETTER_HX_SMARTTEXT_ID` | VARCHAR |  | The SmartText template used to generate the letter |
| 9 | `LETTER_HX_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

