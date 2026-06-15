# UNIV_CHG_LN_DX

> This table contains diagnosis information for one charge in the Universal Charge Line (UCL) masterfile.

**Primary key:** `UCL_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK FK→ | The unique ID associated with the charge record. |
| 2 | `LINE` | INTEGER | PK | Each charge line (UCL) can have multiple diagnoses associated with it. The combination of UCL_ID and LINE make up a unique identifier for this diagnosis. |
| 3 | `DIAGNOSIS_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `DIAGNOSIS_QUAL_C_NAME` | VARCHAR | org | The qualifier for the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `UCL_ID` | [CLARITY_UCL](CLARITY_UCL.md) | sole_pk | high |

