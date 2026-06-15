# IMP_STERILIZE_CHECKPTS

> This tables stores the checkpoints for implants when using a sterilization protocol such as Immediate Use Steam Sterilization (IUSS).

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the implant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMP_STERILIZE_CHECKPTS_C_NAME` | VARCHAR | org | This column stores the checkpoints for implants when using a sterilization protocol such as Immediate Use Steam Sterilization (IUSS). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

