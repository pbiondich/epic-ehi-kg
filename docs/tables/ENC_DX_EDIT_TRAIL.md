# ENC_DX_EDIT_TRAIL

> This table stores the audit trail information for encounter diagnosis edits. In order to report on diagnosis edits, this table can be linked with PAT_ENC_DX. This linking can be done using the PAT_ENC_CSN_ID and DX_EDIT_UNIQUE columns in this table along with the PAT_ENC_CSN_ID and DX_UNIQUE columns in the PAT_ENC_DX table.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the unique contact identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `DX_EDIT_CHRONIC_YN` | VARCHAR |  | Indicates whether or not the edited diagnosis is chronic. Y indicates that the edited diagnosis is chronic. N indicates that the edited diagnosis is not chronic. |
| 4 | `DX_EDIT_PRIMDX_YN` | VARCHAR |  | Indicates whether or not the edited diagnosis is primary. Y indicates that the edited diagnosis is primary. N indicates that the edited diagnosis is not primary. |
| 5 | `DX_EDIT_STATUS_C_NAME` | VARCHAR |  | Stores category numbers for past values of the Differential diagnosis status. |
| 6 | `DX_EDIT_ED_YN` | VARCHAR |  | This column stores audit trail information for encounter diagnosis edits, particularly the ED Diagnosis flag of the associated edit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

