# V_EHI_OVR_EMB_PAT_FILTER

> This view was created to handle filtering embryology results for patients and filtering out deidentified genetic contributor data.

**Primary key:** `RESULT_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `EMB_RSLT_GC_PAT_ID` | VARCHAR | FK→ | Stores the EPT patients who are a genetic contributor for an embryology procedure |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EMB_RSLT_GC_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

