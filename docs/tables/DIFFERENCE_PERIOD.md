# DIFFERENCE_PERIOD

> Information about the difference period.

**Primary key:** `DIFF_PERIOD_ID`  
**Columns:** 9  
**Org-specific columns:** 1  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DIFF_PERIOD_ID` | NUMERIC | PK | The unique identifier (.1 item) for the difference period record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The patient this difference period is for. |
| 3 | `START_DATE` | DATETIME |  | The date the difference period begins on. |
| 4 | `END_DATE` | DATETIME |  | The date the difference period ends (inclusive). |
| 5 | `VIEW_START_DATE` | DATETIME |  | The computed start date for end-user viewing. |
| 6 | `VIEW_END_DATE` | DATETIME |  | The computed end date (inclusive) of the difference period for displaying to end users. |
| 7 | `ROSTER_IDENTIFIER_C_NAME` | VARCHAR | org | The roster identifier this assignment and attribution difference period is related to. |
| 8 | `VALUE_BASED_PROGRAM_ID` | NUMERIC |  | The value based program identifier. |
| 9 | `VALUE_BASED_PROGRAM_ID_RECORD_NAME` | VARCHAR |  | The name of the program record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [DIFFERENCE_PERIOD_EVENT](DIFFERENCE_PERIOD_EVENT.md) | `DIFF_PERIOD_ID` | high |
| [DIFF_PER_NEW_ATTR_INFO](DIFF_PER_NEW_ATTR_INFO.md) | `DIFF_PERIOD_ID` | high |

