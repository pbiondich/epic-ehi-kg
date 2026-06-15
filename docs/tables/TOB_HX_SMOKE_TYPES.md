# TOB_HX_SMOKE_TYPES

> Tobacco History data for Smoking History Types that are not cigarettes.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `TOB_QUESN_TYP_C_NAME` | VARCHAR | org | The tobacco type the data represents, same category as EPT 19211. |
| 4 | `TOB_HX_TYP_START_DATE` | DATETIME |  | Start date for the use of the specified tobacco type. Stored as a fuzzy date. DTE is followed with a [ followed by the precision. 1 - Year, 2 - Month, 3 - Day. |
| 5 | `TOB_HX_TYP_QUIT_DATE` | DATETIME |  | Quit date for the use of the specified tobacco type. Stored as a fuzzy date. DTE is followed with a [ followed by the precision of the date. 1 - Year, 2 - Month, 3 - Day. |
| 6 | `TOB_HX_TYP_CMT` | VARCHAR |  | Comment for the specified tobacco type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

