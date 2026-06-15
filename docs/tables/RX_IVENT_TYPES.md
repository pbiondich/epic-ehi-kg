# RX_IVENT_TYPES

> The intervention types table contains one record for each intervention and the type associated with the intervention. The primary key for the intervention type table is INTERVENTION_ID, LINE.

**Primary key:** `INTERVENTION_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | NUMERIC | PK FK→ | The unique ID for the intervention. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TYPE_C_NAME` | VARCHAR | org | The type(s) associated with this intervention, indicating the nature of the intervention. |
| 4 | `SUBTYPE_C_NAME` | VARCHAR | org | This is the subtype of the intervention. Use this item along with the type (I RXI 50) to categorize the purpose of the intervention. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

