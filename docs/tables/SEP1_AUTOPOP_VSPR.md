# SEP1_AUTOPOP_VSPR

> This table contains autopopulation data source information for the vasopressor administration data element in the CMS SEP-1 core measure.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VSPR_YN` | VARCHAR |  | The value (either 0-No or 1-Yes) to indicate if an IV or intraosseous vasopressor was administered within the six hours after the Septic Shock Presentation Instant. |
| 4 | `ORDER_MED_ID` | NUMERIC | FK→ | The ID of the order for IV or intraosseous vasopressor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

