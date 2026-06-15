# CANCER_RISK_REQ_MODEL

> This table contains the risk models for patients whose scores were user requested.

**Primary key:** `PAT_ENC_CSN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 4 | `SCORE_REQ_CANCER_RISK_MODEL_C_NAME` | VARCHAR | org | This column stores the risk assessment models whose scores the user requested. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

