# SURGICAL_HX

> The SURGICAL_HX table contains data from medical history contacts entered in clinical system patient encounters. Since one patient encounter may contain multiple medical history contacts, each contact is uniquely identified by a combination of the patient encounter serial number and a line number.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 2 | `LINE` | INTEGER | PK | The line number of the surgical history contact within the encounter. |
| 3 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `SURGICAL_HX_DATE` | VARCHAR |  | The free-text date entered in a patient's Surgical History for the procedure. |
| 5 | `COMMENTS` | VARCHAR |  | Free-text comments entered for the procedure in the surgical history contact. |
| 6 | `PROC_COMMENTS` | VARCHAR |  | Free-text comments entered for the "other" procedure in the patient's surgical history. |
| 7 | `CONTACT_DATE` | DATETIME |  | The contact date of the encounter associated with this surgical history contact. Note: There may be multiple encounters on the same calendar date. |
| 8 | `CM_CT_OWNER_ID` | VARCHAR |  | ID of the deployment owner for this contact. |
| 9 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 10 | `SURGICAL_HX_SRC_C_NAME` | VARCHAR | org | This category number represents the source of entry, the person providing the information, for the surgical history data. |
| 11 | `HX_LNK_ENC_CSN` | NUMERIC | FK→ | The Contact Serial Number of the encounter in which the history was created/edited. If the history was created/edited outside of the context of an encounter, then this column will be blank. |
| 12 | `SURGICAL_HX_SRG_CSN` | NUMERIC |  | Stores the contact serial number of the surgery contact related to the current procedure. |
| 13 | `SURG_LATERALITY_C_NAME` | VARCHAR | org | This category is used to store the laterality for each past surgical record in surgical history. |
| 14 | `SURG_HX_START_DT` | DATETIME |  | The starting date for the range of possible dates extracted from the free text date entered in column SURGICAL_HX_DATE. It is filled in automatically when the patient's history is saved. The ending date is in column SURG_HX_END_DT. |
| 15 | `SURG_HX_END_DT` | DATETIME |  | The ending date for the range of possible dates extracted from the free text date entered in column SURGICAL_HX_DATE. It is filled in automatically when the patient's history is saved. The starting date is in SURG_HX_END_DT. |
| 16 | `SURG_HX_ORDER_ID` | NUMERIC |  | The unique ID of the order related to the current surgical history procedure |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HX_LNK_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

