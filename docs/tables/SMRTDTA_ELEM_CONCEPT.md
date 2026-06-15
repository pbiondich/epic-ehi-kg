# SMRTDTA_ELEM_CONCEPT

> This table is a bridge between concept context SmartData element values and the source SmartData element value records.

**Primary key:** `HLV_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the value record. |
| 2 | `PARENT_HLV_ID` | NUMERIC |  | The unique ID of the linked concept record that is associated with the SmartData element value. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record linked to the SmartData element. This column is frequently used to link to the PATIENT table. |
| 4 | `ELEMENT_ID` | VARCHAR | FK→ | The SmartData identifier (SDI) for this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ELEMENT_ID` | [OR_PNDS](OR_PNDS.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

