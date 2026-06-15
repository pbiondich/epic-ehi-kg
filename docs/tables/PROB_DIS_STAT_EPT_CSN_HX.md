# PROB_DIS_STAT_EPT_CSN_HX

> This table extracts a list of patient contact serial numbers (EPT CSNs) indicating the visits in which clinicians have edited the disease status for a problem on a patient's problem list.

**Primary key:** `PROBLEM_LIST_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the problem record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `HX_DISEASE_STAT_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the patient contact serial number (EPT CSN) of a visit in which a clinician edited the disease status for a problem on a patient's problem list. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HX_DISEASE_STAT_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

