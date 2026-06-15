# HH_OASIS_ICD10_DX

> This table contains all of the clinical Outcome and Assessment Information Set (OASIS) ICD-10 diagnoses entered by a field nurse and edited in Diagnosis Review. The first diagnosis for a given patient encounter is the primary diagnosis. The next 5 are the diagnoses that will go on the OASIS submission. Anything after the sixth diagnosis for a given encounter is merely reportable.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `OASIS_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 7 | `OASIS_DX_START_DATE` | DATETIME |  | Start date of M1021 and M1023 diagnoses. |
| 8 | `OASIS_DX_SCR_C_NAME` | VARCHAR | org | The category number for the symptom control rating for M1021 and M1023. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID) |
| 9 | `OASIS_DX_FLAG_C_NAME` | VARCHAR | org | The Flag item is a customer defined category list that can be used to further describe a diagnosis entry. An example of the use of this item would be for flagging a diagnosis as an exacerbation or onset. The flag will be carried over to the plan of care. |
| 10 | `OASIS_DX_OTHER_1_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 11 | `OASIS_DX_OTHER_2_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

