# RISK_ADJ_EVAL_VERS_INFO

> Stores contact specific identification information for risk adjustment data.

**Primary key:** `SUMMARY_DATA_ID`, `CONTACT_DATE_REAL`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the summary record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SUMMARY_DATA_ID` | [RISK_MODEL_REFERENCE_INFO](RISK_MODEL_REFERENCE_INFO.md) | sole_pk | high |

