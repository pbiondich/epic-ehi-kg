# HH_PAT_OTHER_DX

> Contains information from the Home Health Other Diagnoses grid.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONTACT_DATE_REAL` | FLOAT |  | Unique identifier for this contact for this patient. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `OTHER_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `OTHER_DX_START_DT` | DATETIME |  | Other diagnosis start date. |
| 5 | `OTHER_DX_SEVERITY` | INTEGER |  | Other diagnosis severity, 0-4. |
| 6 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 7 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 8 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |
| 9 | `OTHER_DX_FLAG_C_NAME` | VARCHAR | org | A customer-defined addition to a diagnosis entry, such as flagging a diagnosis as an exacerbation or onset. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

