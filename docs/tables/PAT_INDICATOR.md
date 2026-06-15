# PAT_INDICATOR

> The PAT_INDICATOR table contains information about your patient genomic indicator records. These include disease-related and drug-related genomic indicators linked to patients.

**Primary key:** `PAT_INDICATOR_ID`  
**Columns:** 11  
**Joined by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_INDICATOR_ID` | NUMERIC | PK | This column contains the unique identifier (.1 item) for the pt indicators record. |
| 2 | `GENOMIC_INDICATR_ID` | NUMERIC |  | This column contains the Genomic Indicator linked to this record. |
| 3 | `GENOMIC_INDICATR_ID_RESOLVED_PAT_FRIENDLY_NAME` | VARCHAR |  | This column provides an always populated name column that prioritizes the patient friendly name and if there is none specified, falls back to the clinical name. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The column contains the unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 5 | `OVERVIEW_NOTE_ID` | VARCHAR |  | This column contains the overview note for the genomic indicator as linked to the patient. Patient-specific details about the genomic indicator are stored in the note networked to this item. |
| 6 | `RECORD_CREATION_DT` | DATETIME |  | This column contains the date the record was created. |
| 7 | `INSTANT_OF_UPD_DTTM` | DATETIME (Local) |  | This column contains the instant the record was last locked/unlocked. |
| 8 | `CREATION_SOURCE_C_NAME` | VARCHAR |  | The creation source for this patient genomic indicator. Blank values are treated as manually created indicators by the translation engine. |
| 9 | `ACT_SCORE_LOWER` | NUMERIC |  | This item represents the lower bound of the manually entered activity score for the patient genomic indicator. |
| 10 | `ACT_SCORE_UPPER` | NUMERIC |  | This item represents the upper bound of the manually entered activity score for the patient genomic indicator. |
| 11 | `ACT_SCORE_SOURCE_C_NAME` | VARCHAR |  | This item represents whether the activity score in PGI 1040/1041 was sourced from manual entry, genotype-activity score mapping tables, or directly from a variant result. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (10)

| From | Column | Confidence |
|------|--------|------------|
| [INDICATOR_REL_ORD_DOC](INDICATOR_REL_ORD_DOC.md) | `PAT_INDICATOR_ID` | high |
| [INDICATOR_REL_ORD_RSLT](INDICATOR_REL_ORD_RSLT.md) | `PAT_INDICATOR_ID` | high |
| [INDICATOR_REL_ORD_TBL](INDICATOR_REL_ORD_TBL.md) | `PAT_INDICATOR_ID` | high |
| [INDICATOR_REL_ORD_VAL](INDICATOR_REL_ORD_VAL.md) | `PAT_INDICATOR_ID` | high |
| [INDICATOR_REL_ORD_VARIANT](INDICATOR_REL_ORD_VARIANT.md) | `PAT_INDICATOR_ID` | high |
| [INDICATOR_REL_RSLT_SRC](INDICATOR_REL_RSLT_SRC.md) | `PAT_INDICATOR_ID` | high |
| [INDICATOR_REL_VARIANT_SRC](INDICATOR_REL_VARIANT_SRC.md) | `PAT_INDICATOR_ID` | high |
| [IND_INTERPRT_ACTV_SCORE](IND_INTERPRT_ACTV_SCORE.md) | `PAT_INDICATOR_ID` | high |
| [PAT_INDICATOR_INFO](PAT_INDICATOR_INFO.md) | `PAT_INDICATOR_ID` | high |
| [V_PAT_IND_AUD_TRL_VALS](V_PAT_IND_AUD_TRL_VALS.md) | `PAT_INDICATOR_ID` | high |

