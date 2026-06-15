# OR_LNLG_CELL_SVR_AUTO

> The OR_LNLG_CELL_SVR_AUTO table contains information whether the blood was simply saved using cell saver equipment or whether it was automatically reinfused during the surgery.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CELL_SVR_AUTOTRSF_C_NAME` | VARCHAR | org | The cell saver autotransfusion category ID for whether the blood was simply saved using cell saver equipment or whether it was automatically reinfused during the surgery. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

