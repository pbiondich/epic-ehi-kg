# TOB_PACKYEARS_DATA

> Contains the tobacco history for the patient's cigarette use for their pack year history.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `TOB_HX_PACKS_PER_DAY_NUM` | NUMERIC |  | Stores the packs per day for the current tobacco episode. Can be converted to cigarettes per day for display or entry via LQH settings. |
| 4 | `TOB_HX_START_DATE` | DATETIME |  | Start date for the tobacco episode, stored as a fuzzy date. DTE is followed with a [ followed by the precision. 1 - Year, 2 - Month, 3 - Day. |
| 5 | `TOB_HX_END_DATE` | DATETIME |  | End date for the tobacco episode, stored as a fuzzy date. DTE is followed with a [ followed by the precision. 1 - Year, 2 - Month, 3 - Day. |
| 6 | `TOB_HX_YEARS_NUM` | NUMERIC |  | Stores the years smoking for the current tobacco episode. Will not be set if TOB_HX_START_DATE and TOB_HX_END_DATE are set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

