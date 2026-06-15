# ORDER_RAD_MODS

> ORDER_RAD_MODS stores the list of modifiers that were added within radiology as opposed to standard order entry.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of modifiers on an order added in radiology information system. |
| 3 | `MODIFIER_ID` | VARCHAR | FK→ | The modifier added in radiology. |
| 4 | `MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MODIFIER_ID` | [CLARITY_MOD](CLARITY_MOD.md) | sole_pk | high |
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

