# ORD_AUD_ASGN_POOLS

> This table contains the audit information about the list of assigned pools for an imaging procedure.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASGN_POOLS_EXTERNAL_VALUES` | VARCHAR |  | Audit item for list of assigned pools (external values) for an imaging procedure. The values are delimited by "^". The source item is located at RIS_ASGN_POOL.RAD_ASGN_PLS_ID. This column shows the translated external value as of when the column was last extracted. |
| 4 | `ASGN_POOLS_PLS_IDS` | VARCHAR |  | Audit item for list of assigned pools (IDs) for an imaging procedure. The values are delimited by "^". The source item is located at RIS_ASGN_POOL.RAD_ASGN_PLS_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

