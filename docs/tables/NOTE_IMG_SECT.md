# NOTE_IMG_SECT

> This table contains information about imaging orders resulted using the Imaging SmartSection.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMG_SECT_RESULT_NOTE_CSN_ID` | NUMERIC |  | The unique contact serial number of the result note associated with the imaging order. |
| 4 | `IMG_SECT_ORDER_ID` | NUMERIC |  | The unique ID of the imaging order record for this row. This column is frequently used to link to the ORDERS table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

