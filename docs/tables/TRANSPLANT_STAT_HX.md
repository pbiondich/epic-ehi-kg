# TRANSPLANT_STAT_HX

> This table contains information about a transplant episode's phase, status, and reason.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID of the episode of care record. |
| 2 | `LINE` | INTEGER | PK | Each line represents a change in status for this transplant episode. |
| 3 | `TX_STAGE_C_NAME` | VARCHAR |  | The phase of the transplant episode, e.g. Pre-Evaluation, Evaluation, Transplanted. |
| 4 | `TX_STAT_DT` | DATETIME |  | Effective date associated with the patient's transplant phase, status, and reason. |
| 5 | `TX_STATUS_OUT_C_NAME` | VARCHAR | org | Status associated with the patient's transplant phase and reason. |
| 6 | `TX_STAT_UPD_USER_ID` | VARCHAR |  | The unique ID of the user who updated the transplant phase, status, or reason. |
| 7 | `TX_STAT_UPD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `TX_STAT_UPD_INST` | DATETIME (Local) |  | The instant the transplant phase, status, or reason was updated. |
| 9 | `TX_STATUS_REASON_C_NAME` | VARCHAR | org | Reason for the patient's transplant phase and status. |
| 10 | `TXP_PHASE_ENC_CSN` | NUMERIC | FK→ | Contact Serial Number (CSN) for the encounter where the transplant phase, status, or reason was changed. This is used in the transplant history audit trail. It is also used to provide a link to the encounter in which the phase was changed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TXP_PHASE_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

