# ORDER_PATHWAY

> If this order record is part of a patient's Pathway, then this table contains the IDs of the Pathway records that contain this order.

**Primary key:** `ORDER_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of this order record. |
| 2 | `PATHWAY_TRG_ID` | NUMERIC |  | The unique ID of the patient-level SmartGroup that contains this order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

