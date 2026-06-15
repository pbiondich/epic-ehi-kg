# ABN_ORDERS

> The ABN_ORDERS table contains the orders associated with Advanced Beneficiary Notice note records.

**Primary key:** `ABN_NOTE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ABN_NOTE_ID` | VARCHAR | PK FK→ | The unique ID of the note (HNO) record that contains the Advance Beneficiary Notice (ABN) information. |
| 2 | `LINE` | INTEGER | PK | The line number of the order ID associated with the ABN record. |
| 3 | `ORDER_ID` | NUMERIC | shared | The order ID that is associated with the ABN record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ABN_NOTE_ID` | [ABN_NOTES](ABN_NOTES.md) | sole_pk | high |

