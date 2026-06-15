# PRE_AR_ANES_SUP_UNIT_INFO

> This table contains supplemental Anesthesia related information for temporary transactions.

**Primary key:** `TAR_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the charge session record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UNIT_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `UNIT_PROC_QUANTITY` | INTEGER |  | The supplemental unit procedure quantity for the anesthesia supplemental procedure. |
| 5 | `UNIT_PROC_UNITS` | INTEGER |  | The supplemental unit procedure units for the anesthesia supplemental procedure. |
| 6 | `UNIT_PROC_DESC` | VARCHAR |  | The supplemental unit procedure description for the anesthesia supplemental procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

