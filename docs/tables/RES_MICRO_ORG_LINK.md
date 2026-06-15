# RES_MICRO_ORG_LINK

> Table for various results (workcard isolates, workcard actions, susceptibilities) linked to a culture (organism) result.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LINKED_RESULTS_ID` | VARCHAR |  | The identifiers for results linked to this organism result. On an isolate result record, this item will link to all organism workcards and all susceptibility tests related to that result. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

