# PLAN_NO_SUPPORT_YR_AUDIT

> This table contains the results of health plan audits for risk adjustment categories that cannot be found on supporting evidence that can be submitted in the plan year, as of the given review date with the evidence available.

**Primary key:** `SUMMARY_DATA_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the summary record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `AUDIT_TEMPLATE_VERSION_C_NAME` | VARCHAR | org | The category version category ID for the category template determined during a health plan audit that is not supported with evidence for submission for this plan year. |
| 5 | `LAST_REVIEW_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the user last reviewed and marked the category as not being supported for this plan year. |
| 6 | `LAST_REVIEW_COMMENT` | VARCHAR |  | The review comments entered by the last audit reviewer about the category decision. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SUMMARY_DATA_ID` | [RISK_MODEL_REFERENCE_INFO](RISK_MODEL_REFERENCE_INFO.md) | sole_pk | high |

