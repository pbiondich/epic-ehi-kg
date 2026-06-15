# PTENC_ALT_REF_INFO

> Referring provider alternate information.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 3  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `ALT_REF_PROV_SEX_C_NAME` | VARCHAR | org | The category number of the sex of the patient's alternate referring provider for an encounter. This column is used to link to the ZC_SEX table. |
| 3 | `ALT_REF_PROV_TITL_C_NAME` | VARCHAR | org | The category number of the title of the patient's alternate referring provider for an encounter. This column is used to link to the ZC_ALT_ORD_PRV_TIT table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

