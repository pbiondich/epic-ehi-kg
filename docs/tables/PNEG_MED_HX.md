# PNEG_MED_HX

> The PNEG_MED_HX table contains data from pertinent negatives medical history contacts entered in clinical system patient encounters. Since one patient encounter may contain multiple medical history contacts, each contact is uniquely identified by a patient encounter serial number and a line number.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PNEG_MED_HX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `PNEG_MED_HX_DT` | DATETIME |  | The entry date for a patient's pertinent negative medical history for a diagnoses. |
| 5 | `PNEG_MED_HX_CMT` | VARCHAR |  | Free text comments entered for the diagnoses in a patient's pertinent negative medical history. |
| 6 | `PNEG_MED_HX_ANNO` | VARCHAR |  | The annotation for the diagnoses in a patient's pertinent negative medical history. |
| 7 | `HX_LNK_ENC_CSN` | NUMERIC | FK→ | The Contact Serial Number of the encounter in which the history was created/edited. If the history was created/edited outside of the context of an encounter, then this column will be blank. |
| 8 | `PNEG_MED_HX_SRC_C_NAME` | VARCHAR | org | The Pertinent Negative Medical History Source for the Pertinent Negative Medical History contacts. This column defines whether history information was entered by the patient versus the provider or a legal guardian. This can be used to differentiate which information was entered directly by the patient via MyChart or kiosks versus was entered by the provider. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HX_LNK_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

