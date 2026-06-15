# IMP_AUDIT_TRAIL

> Table to store Implants (IMP) auditing items.

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the implant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_NEW_ITEM_VAL` | VARCHAR |  | Stores the new value of the item that was changed. |
| 4 | `AUDIT_OLD_ITEM_VAL` | VARCHAR |  | Stores the old value of the item that was changed |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

