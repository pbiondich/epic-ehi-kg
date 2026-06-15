# DENTAL_PROC_MODIFIERS

> This table contains modifiers associated with dental procedures.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENTAL_PROC_MODIFIER_ID` | VARCHAR |  | This item stores the procedure modifiers for dental procedures. These modifiers may be used to provide details about dental procedures. |
| 4 | `DENTAL_PROC_MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

