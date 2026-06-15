# HH_INTVTN_CONTACT

> Contains Home Health care plan intervention contact information.

**Primary key:** `INTERVENTION_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | VARCHAR | PK FK→ | Unique identifier for the care plan intervention. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PERFORMED_YN` | VARCHAR |  | Care plan intervention contact interventions performed. Yes or no. |
| 4 | `VARIANCE_CODE_C_NAME` | VARCHAR | org | Care plan intervention contact variance code. Links to category table ZC_VARIANCE_CODE. |
| 5 | `CNCT_SEQUNCE_NUM` | VARCHAR |  | Care plan intervention contact sequence number. |
| 6 | `VISITS_DEFERRED_YN` | VARCHAR |  | Care plan intervention contact visits deferred. Yes or no. |
| 7 | `CONTACT_NOTES_ID` | VARCHAR |  | Care plan intervention contact notes ID. |
| 8 | `DOC_SOURCE_C_NAME` | VARCHAR |  | This item tracks the source of intervention documentation among multiple platforms. The most recent documentation source will overwrite the previous one if two platforms are used for the same intervention. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

