# TRANSPLANT

> This table contains the basic information about each transplant patient encounter in your system.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique system identifier for the patient encounter. Contact serial number is unique across all patients and all contacts. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date on which the patient encounter took place. |
| 5 | `ORGAN_TRANSPLAN_C_NAME` | VARCHAR | org | The organ which was transplanted. |
| 6 | `ORGAN_SOURCE_C_NAME` | VARCHAR | org | The source of where the transplanted organ came from. |
| 7 | `TRANSPLANT_DT` | DATETIME |  | The actual date on which the operation took place. |
| 8 | `PRIOR_REJECTION_YN` | VARCHAR |  | Set to Y if the patient has had a prior rejection episode. |
| 9 | `ANTIGEN_MATCH_C_NAME` | VARCHAR | org | Antigens encourage an immune response in the body. This column contains information about the patient's antigen match level. |
| 10 | `TRANSPLANT_LOC_C_NAME` | VARCHAR | org | This column contains information about the location of the transplanted organ. For example, "bilateral", "center", etc. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

