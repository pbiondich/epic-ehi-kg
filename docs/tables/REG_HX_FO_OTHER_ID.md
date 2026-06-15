# REG_HX_FO_OTHER_ID

> This table shows information for the filing order change events from tracking registration history event notes. It displays the "other" filing order, and can be used in conjunction with REG_HX_FO_OLD and REG_HX_FO_NEW, which display the old and new filing order. In most cases, the "other" filing order is the account filing order at the time of filing order change.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REG_HX_FO_OTHER_ID` | INTEGER |  | The "other" filing order, which can be used in conjunction with REG_HX_FO_OLD and REG_HX_FO_NEW, displays a third relevant filing order to the change. In most cases, the "other" filing order is the account filing order at the time of filing order change. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

