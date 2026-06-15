# TXT_AUTHPR_OTH_IDS

> When the authorizing provider for a prescription is not in the provider database, a free-text provider may be entered in ambulatory pharmacy. Any IDs that are collected for that provider are stored in this table.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TXT_AUTHPROV_OTH_ID` | VARCHAR |  | The other ID of the authorizing provider if the provider does not exist in Epic. This column stores the ID type for other IDs the provider may have (for instance, a state-specific ID number, or the Texas DPS number). |
| 4 | `TXT_AUTHPROV_TYP_ID` | NUMERIC |  | The ID type for other IDs of the authorizing provider if the provider does not exist in Epic. This column stores the ID type for other IDs the provider may have (for instance, a state-specific ID number, or the Texas DPS number). |
| 5 | `TXT_AUTHPROV_TYP_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

