# SEP1_AUTOPOP_ANTIBIO

> This table contains autopopulation data source information for broad spectrum or other antibiotic administration data element in the CMS SEP-1 core measure.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANTIBIO_YN` | VARCHAR |  | The value (either 0-No or 1-Yes) to indicate if a broad spectrum or other antibiotic was started within 24 hours before or three hours after the Severe Sepsis Presentation Instant. |
| 4 | `ORDER_MED_ID` | NUMERIC | FK→ | The order ID of the broad spectrum or other antibiotic order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

