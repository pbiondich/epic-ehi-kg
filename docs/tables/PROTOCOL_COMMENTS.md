# PROTOCOL_COMMENTS

> This table stores the overall comments entered for a QuickForm-based protocol. SmartForm-based protocols do not have the ability to enter this field.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record for this row. This column is frequently used to link to the ORDER_PROC table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROTOCOL_COMMENTS` | VARCHAR |  | The free text, general comments entered by a physician performing a protocol on an imaging procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

