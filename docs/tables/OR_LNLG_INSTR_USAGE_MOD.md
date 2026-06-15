# OR_LNLG_INSTR_USAGE_MOD

> This item stores additional information about how an instrument was used (e.g. was the instrument cleaned before closing?), and it can be used for Surgical Site Infection (SSI) reporting. Intra-op nurses will typically document this information in the Site Completion form.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INSTR_USAGE_MOD_C_NAME` | VARCHAR | org | Indicate how the instrument was used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

