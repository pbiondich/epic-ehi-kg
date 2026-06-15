# HH_INTVTN_HX_CONT

> Contains Home Health care plan intervention contact history information.

**Primary key:** `INTERVENTION_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | VARCHAR | PK FK→ | Unique identifier for the care plan intervention. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_CNCT_SQNCE_NUM` | VARCHAR |  | Care plan intervention history-contact serial number. |
| 4 | `HX_ADDND_LN` | INTEGER |  | Care plan intervention history-addendum line. |
| 5 | `HX_PERFORMED_YN` | VARCHAR |  | Care plan intervention contact history-interventions performed. Yes or no. |
| 6 | `HX_VARIANCE_C_NAME` | VARCHAR | org | Care plan intervention contact history-variance code. Links to category table ZC_VARIANCE_CODE. |
| 7 | `HX_VISITS_DEFER_YN` | VARCHAR |  | Care plan intervention contact history-visits deferred. Yes or no. |
| 8 | `HX_NOTES_CONTACTS` | VARCHAR |  | Care plan intervention contact history-notes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

