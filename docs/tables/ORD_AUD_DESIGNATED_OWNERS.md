# ORD_AUD_DESIGNATED_OWNERS

> This table contains the audit information about the designated owners who own this imaging study.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASGN_OWNERS_EXTERNAL_VALUES` | VARCHAR |  | Audit information about the designated owners (external value) who own this imaging study. The values are delimited by "^". The source item is located at ORDER_RAD_OWNERS.OWNER_PROV_ID. This column shows the translated external value as of when the column was last extracted. |
| 4 | `ASGN_OWNERS_SER_IDS` | VARCHAR |  | Audit information about the designated owners (IDs) who own this imaging study. The values are delimited by "^". The source item is located at ORDER_RAD_OWNERS.OWNER_PROV_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

