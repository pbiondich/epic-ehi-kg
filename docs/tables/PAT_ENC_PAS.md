# PAT_ENC_PAS

> PAS items for a patient encounter.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `AMBULANCE_INCIDENT_NUM` | VARCHAR |  | The unique identifier of a patient's journey, via ambulance, to a place where the patient received care. |
| 3 | `AMBULANCE_ORG_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 4 | `AMBULANCE_VEHIC_NUM` | VARCHAR |  | The ambulance vehicle number for this encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

