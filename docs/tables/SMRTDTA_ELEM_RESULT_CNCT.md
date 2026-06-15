# SMRTDTA_ELEM_RESULT_CNCT

> This table is a bridge between result contact context SmartData element values and the source result record contacts.

**Primary key:** `HLV_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the value record. |
| 2 | `FINDING_CSN_ID` | NUMERIC |  | The unique contact serial number for the result contact that is associated with the SmartData element value. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 3 | `FINDING_ID` | NUMERIC | shared | The unique ID of the linked result record that is associated with the SmartData element value. |
| 4 | `ELEMENT_ID` | VARCHAR | FK→ | The SmartData identifier (SDI) for this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ELEMENT_ID` | [OR_PNDS](OR_PNDS.md) | sole_pk | high |

