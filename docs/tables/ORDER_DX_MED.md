# ORDER_DX_MED

> The ORDER_DX_MED table enables you to report on the diagnoses associated with medications ordered in clinical system (prescriptions). Since one medication order may be associated with multiple diagnoses, each row in this table is one medication - diagnosis relation. We have also included patient and contact identification information for each record. Note that system settings may or may not require that medications be associated with diagnoses. This table contains only information for those medications and diagnoses that have been explicitly associated. Check with your clinical system Application Administrator to determine how your organization has this set up.

**Primary key:** `ORDER_MED_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the medication order (prescription) record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 5 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `DX_QUALIFIER_C_NAME` | VARCHAR | org | The category ID of the qualifier associated with the diagnosis. |
| 7 | `DX_CHRONIC_YN` | VARCHAR |  | Indicates whether the associated diagnosis is chronic. |
| 8 | `COMMENTS` | VARCHAR |  | Free text comments added when the prescription was ordered or discontinued. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

