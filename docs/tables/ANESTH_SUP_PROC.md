# ANESTH_SUP_PROC

> This table is used to track anesthesia supplemental unit procedures.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the transaction record for this row. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 4 | `SUP_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 5 | `SUP_PROC_QUANTITY` | NUMERIC |  | The quantity of this supplemental procedure. |
| 6 | `SUP_PROC_UNITS` | NUMERIC |  | The number of units of this supplemental procedure. |
| 7 | `SUP_PROC_DESC` | VARCHAR |  | The description for this supplemental procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

