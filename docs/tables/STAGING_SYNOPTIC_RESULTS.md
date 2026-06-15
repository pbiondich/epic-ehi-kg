# STAGING_SYNOPTIC_RESULTS

> Synoptic results imported into this cancer stage.

**Primary key:** `STAGE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `STAGE_ID` | NUMERIC | PK shared | The unique identifier for the stage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_ID` | NUMERIC | shared | Store the order IDs of the synoptic results whose data was pulled into the cancer stage. |
| 4 | `ORDER_CONTACT_DATE_REAL` | NUMERIC |  | Stores the order date information (DTE) of the synoptic results whose data was pulled into the cancer stage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

