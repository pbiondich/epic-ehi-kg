# RFL_ADJ_STRINGS

> Adjudication strings for the referral.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | Unique ID of the referral. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADJ_INT_FEE_SCHD_ID` | NUMERIC |  | Adjudication internal fee schedule. |
| 4 | `ADJ_INT_FEE_SCHD_ID_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 5 | `ADJ_PROCEDURES_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 6 | `ADJ_INC_BKT_STR` | VARCHAR |  | Adjudication increment bucket string. |
| 7 | `ADJ_ALLOWED_AMT_LVL` | VARCHAR |  | Allowed amount adjudication levels. |
| 8 | `ADJ_PRICING_ATRIB` | VARCHAR |  | Adjudication pricing attributes. |
| 9 | `ADJ_PAT_PAY_STR` | VARCHAR |  | Patient payment adjudication string. |
| 10 | `ADJ_ALLOWED_AMT_STR` | VARCHAR |  | Allowed amount adjudication string. |
| 11 | `ADJ_REV_CD_ID` | NUMERIC |  | Adjudication Revenue codes |
| 12 | `ADJ_REV_CD_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 13 | `ADJ_PROC_MODS` | VARCHAR |  | Adjudication procedure modifiers |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

