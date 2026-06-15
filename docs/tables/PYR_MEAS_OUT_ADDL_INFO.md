# PYR_MEAS_OUT_ADDL_INFO

> Stores the record-level item type and code pairs that could be imported by payers.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDL_ITEM_TYPE` | VARCHAR |  | Contains the descriptor for what data element the record-level additional item represents. |
| 4 | `ADDL_ITEM_CODE` | VARCHAR |  | Contains the value for the additional record-level item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

