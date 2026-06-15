# PT_DIALYSIS_HX

> *** Soon to be DEPRECATED *** As part of an ongoing conversion, the data in this table will be transitioned to a different data structure. Use V_PAT_DIALYSIS_HISTORY to accurately report on all historic and new dialysis data. Patient's dialysis history.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | ID of the deployment owner for this contact. |
| 6 | `DIALYSIS_EAF_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 7 | `DIALYSIS_TYPE_C_NAME` | VARCHAR | org | The type of dialysis, such as continuous veno-venous hemofiltration or peritoneal dialysis. |
| 8 | `DIALYSIS_START_DATE` | DATETIME |  | Start date of patient dialysis. |
| 9 | `DIALYSIS_END_DATE` | DATETIME |  | End date for patient dialysis. |
| 10 | `DIALYSIS_COMMENTS` | VARCHAR |  | Additional comments on patient dialysis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

