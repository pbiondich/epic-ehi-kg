# HH_PAT_CSMX_OTH_DX

> This table contains case mix diagnoses information entered for a patient as part of a home health Outcome and Assessment Information Set (OASIS) assessment. The table stores values entered for M0246 for the Other diagnoses for the contact.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This column stores a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `CONTACT_DATE` | DATETIME |  | This column stores the contact date. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |
| 6 | `CASE_MIX_DX1_OTH_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 7 | `CASE_MIX_DX2_OTH_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

