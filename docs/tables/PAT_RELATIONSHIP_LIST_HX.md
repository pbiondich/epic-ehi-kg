# PAT_RELATIONSHIP_LIST_HX

> This table contains historical information about patient relationships. It includes information about relationship types and the dates that the relationships were valid. The records included in this table are Patient Relationships (RLA) records. Multiple lines in this table indicate the history of a relationship and are stored in chronological order (line 1 is the earliest).

**Primary key:** `RELATIONSHIP_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RELATIONSHIP_ID` | NUMERIC | PK | The unique identifier for the patient contact record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RELATION_TO_PAT_C_NAME` | VARCHAR | org | The relationship to patient category ID for the patient contact. |
| 4 | `RELATIONSHIP_START_DATE` | DATETIME |  | The date the patient contact's relation to the patient started. |
| 5 | `RELATIONSHIP_END_DATE` | DATETIME |  | The date the patient contact's relation to the patient ended. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

