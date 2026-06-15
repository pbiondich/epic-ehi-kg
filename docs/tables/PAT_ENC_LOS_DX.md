# PAT_ENC_LOS_DX

> The PAT_ENC_LOS_DX table enables you to report on the diagnoses associated with the level of service (LOS) entered for a patient encounter. This table contains only information for those diagnoses that have been explicitly associated with the LOS.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `DX_UNIQUE` | VARCHAR |  | The unique identifier of the diagnosis associated with the Level of Service (LOS). This value corresponds to the DX_UNIQUE column in the PAT_ENC_DX table. Together with PAT_ENC_CSN_ID, this forms the foreign key to the PAT_ENC_DX table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

