# SSC_GEN_REC_INFO

> The SSC_GEN_REC_INFO table contains one row for each patient-level SmartSet Information record in your system. Each row contains general information that is not specific to any contact such as the record's ID, name, and SmartSet Information type.

**Primary key:** `RECORD_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique ID of the patient-level SmartSet Information record. |
| 2 | `DISPLAY_NAME` | VARCHAR |  | The name of the patient-level SmartSet Information record as it appears in Hyperspace. |
| 3 | `SOURCE_STEP_ID` | NUMERIC |  | The unique ID of the Pathway Step that contains this record. |
| 4 | `SOURCE_SMARTGRP_ID` | NUMERIC |  | The unique ID of the Pathway SmartGroup that contains this record. |
| 5 | `APPLY_INSTANT_DTTM` | DATETIME (Local) |  | The instant the SmartSet Information record was applied to the pathway. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

