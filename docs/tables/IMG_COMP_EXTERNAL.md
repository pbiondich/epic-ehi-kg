# IMG_COMP_EXTERNAL

> This stores comparison study data for externally performed procedures.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMP_EXT_LINE` | INTEGER |  | The line number that corresponds with the patient's list of externally performed studies. Use it to join to the table PAT_IMG_EXT_PROCS on the LINE column. |
| 4 | `EXT_CHNG_AMT_C_NAME` | VARCHAR | org | The comparison studies amount of change category ID for the external procedure order in the COMP_EXT_LINE column. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

