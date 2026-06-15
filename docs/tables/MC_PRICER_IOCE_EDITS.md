# MC_PRICER_IOCE_EDITS

> This table contains edits returned from the CMS Integrated Outpatient Code Editor (IOCE) output from the Epic Pricer during adjudication.

**Primary key:** `PRICER_MSG_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier for the Epic Pricer message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IOCE_EDIT_C_NAME` | VARCHAR |  | Edits returned from the CMS Integrated Outpatient Code Editor (IOCE) output from Epic Pricer. |
| 4 | `IOCE_EDIT_TYPE_C_NAME` | VARCHAR |  | Edit type associated with the edit from IOCE_EDIT_C column. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

