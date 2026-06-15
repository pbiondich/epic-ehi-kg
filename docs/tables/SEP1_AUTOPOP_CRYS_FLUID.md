# SEP1_AUTOPOP_CRYS_FLUID

> This table contains autopopulation data source information for crystalloid fluid administration data element in the CMS SEP-1 core measure.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SEP1_FLUID_ADMIN_C_NAME` | VARCHAR | org | The category value that indicates whether crystalloid fluids were initiated within six hours prior thorugh three hours after the Initial Hypotension Instant or the Septic Shock Presentation Instant, whichever is earlier, and the target ordered volume was completely infused. |
| 4 | `ORDER_MED_ID` | NUMERIC | FK→ | The order ID for crystalloid fluid. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

