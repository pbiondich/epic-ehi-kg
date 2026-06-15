# FINDING_TEXT_GEN

> This table contains the type of summary statement that is associated with a particular finding. The summary statement itself is stored in FINDING_TEXT_GEN_SUMMARY__SUMMARY_TEXT.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TYPE_C_NAME` | VARCHAR |  | The statement type category ID for the procedural finding. The summary statement itself is stored in FINDING_TEXT_GEN_SUMMARY__SUMMARY_TEXT. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

