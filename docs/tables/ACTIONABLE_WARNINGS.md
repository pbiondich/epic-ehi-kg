# ACTIONABLE_WARNINGS

> Table for a related group that stores data about selected action buttons from inline order validations.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WARNING_KEY` | VARCHAR |  | This is the key of a warning shown in the order composer with a selected action button. |
| 4 | `SELECTED_BUTTON_KEY` | VARCHAR |  | This item stores the key which identifies a button that was selected in a warning in the order composer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

