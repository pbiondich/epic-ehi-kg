# SEP1_AUTOPOP_LACTATE

> This table contains autopopulation data source for intial and repeat lactate collection data elements in the CMS SEP-1 core measure.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INIT_LACT_YN` | VARCHAR |  | The value (either 0-No or 1-Yes) to indicate if an initial lactate level was collected within six hours prior through three hours following the Severe Sepsis Presentation Instant. |
| 4 | `INIT_LACT_ORDER_ID` | NUMERIC |  | The order ID for an initial lactate level. |
| 5 | `RE_LACT_YN` | VARCHAR |  | The value (either 0-No or 1-Yes) to indicate if a repeat lactate level was collected. |
| 6 | `RE_LACT_ORDER_ID` | NUMERIC |  | The order ID for repeat lactate level. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

