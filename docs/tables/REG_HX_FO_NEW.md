# REG_HX_FO_NEW

> This table shows information for the filing order change events from tracking registration history event notes. It displays the new filing order and should be used in conjunction with REG_HX_FO_OLD which displays the old filing order.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REG_HX_FO_NEW_ID` | INTEGER |  | Contains new filing order list of coverages for reg notes. Each coverage maps to the COVERAGE table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

