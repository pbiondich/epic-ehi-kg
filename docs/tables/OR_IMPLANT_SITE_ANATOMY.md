# OR_IMPLANT_SITE_ANATOMY

> Stores implant site details in the form of a VEL (anatomy) record.

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the implant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANATOMY_RECORD_ID` | NUMERIC |  | This item stores the VEL record that represents specific implant information. |
| 4 | `ANATOMY_RECORD_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

