# RISK_MODEL_REFERENCE_INFO

> This stores identification information for risk adjustment data records.

**Primary key:** `SUMMARY_DATA_ID`  
**Columns:** 5  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_DATA_ID` | NUMERIC | PK | The unique identifier (.1 item) for the summary record. |
| 2 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 3 | `RISK_DATA_PAT_ID` | VARCHAR | FK→ | The patient associated with this risk adjustment summary. |
| 4 | `RA_RECORD_TYPE_C_NAME` | VARCHAR |  | Stores what kind of summary record this is. |
| 5 | `RECORD_CREATION_DATE` | DATETIME |  | Stores the date the record was created. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `RISK_DATA_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [PLAN_NO_SUPPORT_NA_AUDIT](PLAN_NO_SUPPORT_NA_AUDIT.md) | `SUMMARY_DATA_ID` | high |
| [PLAN_NO_SUPPORT_YR_AUDIT](PLAN_NO_SUPPORT_YR_AUDIT.md) | `SUMMARY_DATA_ID` | high |
| [RISK_ADJ_EVAL_VERS_INFO](RISK_ADJ_EVAL_VERS_INFO.md) | `SUMMARY_DATA_ID` | high |

