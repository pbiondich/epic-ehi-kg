# SMRTDTA_ELEM_PAT_ENTERED

> This table is a bridge between patient entered context SmartData element values and the source patient records.

**Primary key:** `HLV_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the value record. |
| 2 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for the patient encounter contact that is associated with the SmartData element value. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the linked patient record that is associated with the SmartData element value. |
| 4 | `ELEMENT_ID` | VARCHAR | FK→ | The SmartData identifier (SDI) for this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ELEMENT_ID` | [OR_PNDS](OR_PNDS.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

