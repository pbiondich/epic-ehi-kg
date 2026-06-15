# OR_LNLG_INSTR_ISSUE

> This table contains documentation on instrument issues.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INSTR_ISSUE_C_NAME` | VARCHAR | org | This item is used to document if any issues were encountered with a piece of equipment or instrument. |
| 4 | `INSTR_ISSUE_DESC` | VARCHAR |  | This item is used to describe any issues encountered with a piece of equipment or instrument. |
| 5 | `INSTR_ISSUE_REPORTED_TO` | VARCHAR |  | This item is used to document who was informed of issues encountered with a piece of equipment or instrument. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

