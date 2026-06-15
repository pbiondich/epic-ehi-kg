# PREV_FLOWSHEET_AUDIT_LN

> Table to store information about the FSD 2000 audit line preceding the values stored to flowsheets from ProcDoc.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PREV_FLO_AUDIT_LINE` | VARCHAR |  | Tracks the FSD 2000 line that holds the state of the Flowsheet at the time the ProcDoc update was made for this order. It is used to restore the proper data if the order is for some reason changed in regards to the wound, or cancelled. It is stored in the format <FLO row ID>^<FSD 2000 line>. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

