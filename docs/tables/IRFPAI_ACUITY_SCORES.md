# IRFPAI_ACUITY_SCORES

> This table contains patient acuity scoring system data for patients based off of their IRF-PAI.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IRF_SCORE_ACUITY_SYSTEM_ID` | NUMERIC |  | Stores the HDA ID of scoring systems used in IRF score calculations. |
| 4 | `IRF_SCORE_ACUITY_SYSTEM_ID_ACUITY_SYSTEM_NAME` | VARCHAR |  | The name of this HDA record. |
| 5 | `IRF_SCORE_VALUE` | NUMERIC |  | Stores IRF scoring systems' calculated scores. |
| 6 | `SAVE_UTC_DTTM` | DATETIME (UTC) |  | This table stores the instant that the scoring system calculation is saved. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

