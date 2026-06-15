# RES_SUPPLY_USED

> This table contains information that relates to supplies.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SUPPLY_USED_ID` | VARCHAR |  | Stores a list of supplies (SUP) used for a procedure. |
| 4 | `SUPPLY_USED_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 5 | `SUPPLY_TYPE_C_NAME` | VARCHAR | org | Stores the type of supply used, mainly for indexing |
| 6 | `IMPLANT_REC_ID` | VARCHAR |  | Stores the ID of the implant corresponding to this supply. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

