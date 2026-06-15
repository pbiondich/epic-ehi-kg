# EPSD_RHB_CLASS

> This table contains information about a patient's Rehab classifications.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `REHAB_CLSS_PARENT_C_NAME` | NUMERIC |  | The parent group of the patient's classification. |
| 3 | `REHAB_CLSS_ORTHO_C_NAME` | NUMERIC |  | The patient's orthomusculoskeletal sub-classification. |
| 4 | `REHAB_CLSS_NEURO_C_NAME` | NUMERIC |  | The patient's neuro sub-classification. |
| 5 | `REHAB_CLSS_MED_C_NAME` | NUMERIC |  | The patient's medical sub-classification. |
| 6 | `REHAB_CLSS_SPEECH_C_NAME` | NUMERIC |  | The patient's speech sub-classification. |
| 7 | `REHAB_CLSS_DEVELP_C_NAME` | NUMERIC |  | The patient's developmental sub-classification. |
| 8 | `REHAB_CLSS_CHRON_C_NAME` | NUMERIC |  | The chronicity of the patient classification. |
| 9 | `REHAB_CLSS_SURG_C_NAME` | NUMERIC |  | The patient's surgical classification. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

