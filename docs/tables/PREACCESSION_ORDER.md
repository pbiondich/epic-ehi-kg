# PREACCESSION_ORDER

> This table contains the preaccession orders for the specimen. When the specimen is accessioned these orders will be placed on the specimen with the given specimen numbers. After accessioning has occurred the table for the specimen will be cleared.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PREACC_ORD_ID` | NUMERIC |  | Orders associated with this specimen prior to accessioning to help keep track of the specimen number to use. When the orders are accessioned they will be added to the specimen they are on and will use the associated specimen number for the test. When the orders are accessioned, this item will be cleared. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

