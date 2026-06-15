# LOADED_EXTERNAL_CVG_DATA

> Clarity table for no-add single items in LCI.

**Primary key:** `EXTERNAL_CVG_ID`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EXTERNAL_CVG_ID` | NUMERIC | PK shared | The unique identifier for the loaded coverage information record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record linked to the External ID bundle associated with this external coverage data. |
| 3 | `EXT_DEMOG_ID` | NUMERIC |  | The unique ID of the External Demographic Set that this external coverage is loaded to. |
| 4 | `EXTERNAL_CVG_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 5 | `EXTERNAL_CVG_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 6 | `EXTERNAL_CVG_SUB_IDENT` | VARCHAR |  | The ID of the subscriber for the associated external coverage. |
| 7 | `EXT_CVG_SOURCE_SYSTEM_C_NAME` | VARCHAR | org | The external source that sent the external coverage information. |
| 8 | `EXTERNAL_CVG_MEMBER_IDENT` | VARCHAR |  | The member's insurance ID for the associated external coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

