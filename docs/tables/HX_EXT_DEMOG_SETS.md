# HX_EXT_DEMOG_SETS

> A list of all external demographic sets (REQs) that this external coverage has been associated with.

**Primary key:** `EXTERNAL_CVG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EXTERNAL_CVG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the subject name record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_EXT_DEMOG_ID` | NUMERIC |  | The unique IDs of the External Demographic Sets (REQs) that have been associated with this external coverage data record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

