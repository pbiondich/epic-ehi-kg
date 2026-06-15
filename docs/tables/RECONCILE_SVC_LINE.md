# RECONCILE_SVC_LINE

> This table contains service line information for claim reconciliation records.

**Primary key:** `CLAIM_REC_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 15  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_REC_ID` | VARCHAR | PK FK→ | The unique ID of the claim reconciliation record. |
| 2 | `CONTACT_DATE` | DATETIME |  | The contact date of the claim, in external format. |
| 3 | `CONTACT_DATE_REAL` | NUMERIC | PK | The contact date of the claim, in internal format. |
| 4 | `LINE` | INTEGER | PK | The line count of line level procedure codes for this claim reconciliation record. |
| 5 | `LINE_PROC_CODE` | VARCHAR |  | The line level procedure codes for this claim reconciliation record. |
| 6 | `LINE_AMT_SUBMT` | NUMERIC |  | The line level amount submitted by the payer for this claim reconciliation record. |
| 7 | `LINE_AMT_PAID` | NUMERIC |  | The line level amount paid by the payer for this claim reconciliation record. |
| 8 | `LINE_STAT_CODE_C_NAME` | VARCHAR | org | The line level status code for this claim reconciliation record. |
| 9 | `LINE_STATUS_MSG` | VARCHAR |  | The line level textual status message for this claim reconciliation record. |
| 10 | `LINE_STAT_CAT_COD_C_NAME` | VARCHAR | org | The line level status category code for this claim reconciliation record. |
| 11 | `LN_CTRL_NUM` | VARCHAR |  | Stores the American National Standards Institute (ANSI) line item control number for this claim reconciliation record. |
| 12 | `LINE_PROC_MODS` | VARCHAR |  | Procedure modifiers associated with the line specified in the information request. |
| 13 | `LINE_REV_CODE` | VARCHAR |  | Revenue code associated with the line specified in the information request. |
| 14 | `LINE_TOOTH_CODE` | VARCHAR |  | Tooth code associated with the line specified in the information request. |
| 15 | `LINE_TOOTH_SURFACES` | VARCHAR |  | Tooth surface codes associated with the line specified in the information request. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_REC_ID` | [RECONCILE_CLM](RECONCILE_CLM.md) | sole_pk | high |

