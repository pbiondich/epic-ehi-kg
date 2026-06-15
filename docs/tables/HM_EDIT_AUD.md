# HM_EDIT_AUD

> The HM_EDIT_AUD table contains audit information for patient-specific health maintenance topic edits. This includes such information as what topic was edited, the editing user, the edits made, and the instant of the edit.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HM_EDIT_AUD_TPC_ID` | NUMERIC |  | Audit information for patient specific HM edits: the edited topic |
| 4 | `HM_EDIT_AUD_TPC_ID_NAME` | VARCHAR |  | The name of the health maintenance topic. |
| 5 | `HM_EDT_AUD_RECOM_ID` | NUMERIC |  | Audit information for patient specific Health Maintenance edits: the recommendation record. |
| 6 | `HM_EDT_AUD_DUE_DATE` | DATETIME |  | Audit information for patient specific Health Maintenance edits: the specified due date. |
| 7 | `HM_EDIT_AUD_MSG_ID` | VARCHAR |  | Audit information for patient specific Health Maintenance edits: In Basket message record. |
| 8 | `HM_EDT_AUD_REC_CSN` | INTEGER |  | Audit information for patient specific HM edits: the recommendation record's CSN |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

