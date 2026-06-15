# SEP1_AUTOPOP_BLD_CULT

> This table contains autopopulation data source information for blood culture collection data element in the CMS SEP-1 core measure.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BLD_CULT_YN` | VARCHAR |  | The value (either 0-No or 1-Yes) to indicate if blood culture was collected within 24 hours before the Severe Sepsis Presentation Instant or Broad Spectrum or Other Antibiotic Administration Instant through three hours following the Severe Sepsis Presentation Instant. |
| 4 | `ORDER_ID` | NUMERIC | shared | The order ID for blood culture. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

