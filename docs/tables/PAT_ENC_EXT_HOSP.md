# PAT_ENC_EXT_HOSP

> This table contains information on external hospital admission encounters. The information includes the admission and discharge dates along with the admitting hospital.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `EXT_HOSP_NAME_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `HOSP_ADMIT_DATE` | DATETIME |  | Date the patient was admitted to the external hospital. |
| 6 | `HOSP_DISCHRG_DATE` | DATETIME |  | Date the patient was discharged from the hospital. |
| 7 | `CONTACT_TYPE_C_NAME` | VARCHAR | org | The encounter type category number for the encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

