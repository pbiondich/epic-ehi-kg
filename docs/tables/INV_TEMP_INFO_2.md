# INV_TEMP_INFO_2

> The INV_TEMP_INFO_2 table displays template, note, and task information for the given intervention record.

**Primary key:** `INTERVENTION_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | NUMERIC | PK FK→ | The unique identifier for the intervention record. |
| 2 | `INTERVENTION_ID_INTERVENTION_NAME` | VARCHAR |  | This column displays the intervention name. |
| 3 | `INTERVENTION_NAME` | VARCHAR |  | This column displays the intervention name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

