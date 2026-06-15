# PNEG_SURG_HX

> The PNEG_SURG_HX table contains pertinent negative surgical history data from history contacts entered in clinical system patient encounters. Since one patient encounter may contain multiple surgical history contacts, each contact is uniquely identified by a patient encounter serial number and a line number.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PNEG_SURG_HX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `PNEG_SURG_HX_DT` | DATETIME |  | The entry date for a patient's pertinent negative surgical history for a procedure. |
| 5 | `PNEG_SURG_HX_CMT` | VARCHAR |  | Free text comments entered for the patient's pertinent negative surgical history. |
| 6 | `PNEG_SURG_HX_SRC_C_NAME` | VARCHAR | org | The category number for the source of entry for the surgical history. Category table information for this item is stored in the Clarity table ZC_HISTORY_SOURCE. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

