# HNO_ABN_ORD_REASON

> The order reasons on the Advance Beneficiary Notice (ABN) form for why the order failed medical necessity checks.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique ID of the note (HNO) record that contains the Advance Beneficiary Notice (ABN) information. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ABN_ORD_REASONS` | VARCHAR |  | The order reasons listed on the ABN form for the procedures that failed medical necessity checks |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

