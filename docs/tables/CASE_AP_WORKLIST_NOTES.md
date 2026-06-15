# CASE_AP_WORKLIST_NOTES

> The CASE_AP_WORKLIST_NOTES table contains information about the worklist notes for the anatomic pathology case.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the requisition record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTES` | VARCHAR |  | The cumulative notes entered on Anatomic Pathology worklists that record relevant information for the processing of a case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

