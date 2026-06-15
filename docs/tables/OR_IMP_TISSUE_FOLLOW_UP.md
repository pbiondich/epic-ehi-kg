# OR_IMP_TISSUE_FOLLOW_UP

> This table contains documentation regarding follow-up actions for tissue implants.

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier for the implant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TISSUE_FOLLOW_UP_C_NAME` | VARCHAR | org | This item is used to document follow-up status after a tissue has been implanted in a patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

