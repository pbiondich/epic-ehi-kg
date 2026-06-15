# ORD_GEN_PALETTE

> Table to hold items regarding note (HNO) records stored against order (ORD) records.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `GENERIC_NOTES_ID` | VARCHAR |  | Note IDs that contain text generated from Generic Palette SmartForms |
| 4 | `GEN_PAL_NOTE_DAT` | NUMERIC |  | Stores the contact date (DAT) of the note used in the generic palette to document the order. |
| 5 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

