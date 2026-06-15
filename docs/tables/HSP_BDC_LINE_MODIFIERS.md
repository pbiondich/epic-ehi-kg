# HSP_BDC_LINE_MODIFIERS

> This table extracts the comma-delimited list of modifiers that is stored in the Line Modifier (I BDC 291) item for line-level denials. This table will contain one row for each modifier that exists in the list.

**Primary key:** `BDC_ID`, `LINE_COUNT`, `MOD_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the denial or correspondence record. |
| 2 | `LINE_COUNT` | INTEGER | PK | Line number of denial data. There can be multiple lines of denial data and this is the number of the line that enterprise reporting is extracting. |
| 3 | `MOD_LINE` | INTEGER | PK | Multiple modifiers can be associated with a specific line on a denial, and this calculated number acts as a unique identifier for an associated modifier. |
| 4 | `EXT_MODIFIER` | VARCHAR |  | This column stores the external identifier for the associated modifier record. |
| 5 | `MODIFIER_ID` | VARCHAR | FK→ | This column stores the unique internal identifier for the associated modifier. |
| 6 | `MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |
| `MODIFIER_ID` | [CLARITY_MOD](CLARITY_MOD.md) | sole_pk | high |

