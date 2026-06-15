# INDICATOR_REL_ORD_TBL

> Contains the related results for patient genomic indicators in a related multiple table making it possible to determine which orders have which components, values, and variants.

**Primary key:** `PAT_INDICATOR_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_INDICATOR_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the pt indicators record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_PROC_ID` | NUMERIC | FK→ | If lab results or genomic variants triggered this patient genomic indicator to be added, the order ID of the lab results or variants causing this PGI to be added is stored in this item. |
| 4 | `PAT_GENOMICS_IND_SRC_C_NAME` | VARCHAR |  | If the order in the ORDER_PROC_ID column was added manually or by the translation engine. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |
| `PAT_INDICATOR_ID` | [PAT_INDICATOR](PAT_INDICATOR.md) | sole_pk | high |

