# ABN_ORDER_INFO

> This table contains additional information about the order linked to the Advanced Beneficiary Notice (ABN).

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique ID of the note (HNO) record that contains the Advance Beneficiary Notice (ABN) information. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORD_PERF_CSN` | NUMERIC |  | Stores the contact serial number (CSN) for the contact where the order is expected to be performed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

