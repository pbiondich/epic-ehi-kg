# V_EHI_CLM_FILTER_STATIC

> This view supports extracting rich text format (RTF) data for EHI from the claim information masterfile.

**Primary key:** `CLAIM_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier of the claim or claim information record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The patient or member associated with the claim or claim information record. |
| 3 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

