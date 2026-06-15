# OB_EPT_OBST_REV

> This table contains when the patient's OB status was reviewed and by whom.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `VITALS_OB_REV_U_ID` | VARCHAR |  | The unique ID of the user who last reviewed the patient's OB/Gyn status. |
| 4 | `VITALS_OB_REV_U_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `VITALS_OB_REV_TM` | DATETIME (Local) |  | Instant the OB/Gyn status of the patient was reviewed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

