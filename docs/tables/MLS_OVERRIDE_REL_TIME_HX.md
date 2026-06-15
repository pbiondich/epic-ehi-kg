# MLS_OVERRIDE_REL_TIME_HX

> Stores 'related' information for override for multiline sig

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MLS_OVRIDE_REL_DAYS` | INTEGER |  | Contains a list of days that are used to override the frequency specified for the order along with the times in ORD-34636. |
| 4 | `MLS_OVRIDE_REL_TM` | VARCHAR |  | Contains a list of times that are used to override the frequency specified for the order along with the days in ORD-34635. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

