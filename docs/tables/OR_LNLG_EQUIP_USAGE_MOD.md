# OR_LNLG_EQUIP_USAGE_MOD

> This table stores additional information about how a piece of equipment was used. Intra-op nurses will typically document this information in the equipment form.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EQUIP_USAGE_MOD_C_NAME` | VARCHAR | org | This column stores additional information about how a piece of equipment was used. Intra-op nurses will typically document this information in the equipment form. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

