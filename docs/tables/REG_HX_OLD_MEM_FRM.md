# REG_HX_OLD_MEM_FRM

> After a change to a member's effective-from date, this table contains a list of the old member-level effective-from dates for all the member lines on a particular coverage on the patient.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OLD_MEM_EFF_FROM_DT` | DATETIME |  | After a change to a member's effective-from date, this contains a list of the old member-level effective-from dates for all the member lines on a particular coverage on the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

