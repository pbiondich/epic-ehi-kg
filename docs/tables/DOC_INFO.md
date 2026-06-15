# DOC_INFO

> Table for attached documents.

**Primary key:** `RELATIONSHIP_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RELATIONSHIP_ID` | NUMERIC | PK | The unique identifier for the relationship record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ATTACHD_DOC_INFO_ID` | VARCHAR |  | This item holds documents that are attached to the patient contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

