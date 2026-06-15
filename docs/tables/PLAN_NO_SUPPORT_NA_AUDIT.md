# PLAN_NO_SUPPORT_NA_AUDIT

> This table contains the results of health plan audits for risk adjustment categories that do not apply to the member, as of the given review date with the evidence available.

**Primary key:** `SUMMARY_DATA_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the summary record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_TEMPLATE_VERSION_C_NAME` | VARCHAR | org | The category version category ID for the category template determined during a health plan audit that does not apply to the patient. |
| 4 | `LAST_REVIEW_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the user last reviewed and marked the category as not applying to the patient. |
| 5 | `LAST_REVIEW_COMMENT` | VARCHAR |  | The review comments entered by the last audit reviewer about the category decision. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SUMMARY_DATA_ID` | [RISK_MODEL_REFERENCE_INFO](RISK_MODEL_REFERENCE_INFO.md) | sole_pk | high |

