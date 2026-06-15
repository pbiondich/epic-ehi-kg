# CV_CONCEPT_TEXT_GEN

> Stores SDE identifiers and whether they are sending to text generation.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONCEPT_ID_TEXT_GEN` | VARCHAR |  | SmartData Element identifier added/removed from text generation for a form. |
| 4 | `CONCEPT_ADDED_YN` | VARCHAR |  | Whether the associated SDE was added to text generation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

