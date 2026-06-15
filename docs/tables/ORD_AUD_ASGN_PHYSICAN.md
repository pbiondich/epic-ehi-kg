# ORD_AUD_ASGN_PHYSICAN

> This table contains the audit information about the list of assigned physicians for an imaging procedure.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASGN_RADS_EXTERNAL_VALUES` | VARCHAR |  | Audit of the list of providers (external values) assigned to interpret an imaging study. The values are delimited by "^". The source item is located at RIS_ASGN_PROV.RAD_ASGN_PROV_ID. This column shows the translated external value as of when the column was last extracted. |
| 4 | `ASGN_RADS_SER_IDS` | VARCHAR |  | Audit of the list of providers (IDs) assigned to interpret an imaging study. The values are delimited by "^". The source item is located at RIS_ASGN_PROV.RAD_ASGN_PROV_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

