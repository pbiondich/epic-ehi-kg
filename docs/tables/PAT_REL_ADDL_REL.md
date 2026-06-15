# PAT_REL_ADDL_REL

> This table contains information about patient relationships beyond the primary relationship. It includes information about relationship types and the dates that the relationships were valid. The records included in this table are Patient Relationships (RLA) records.

**Primary key:** `RELATIONSHIP_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RELATIONSHIP_ID` | NUMERIC | PK | The unique identifier for the relationship record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDL_REL_C_NAME` | VARCHAR | org | Describe the patient contact's relation to the patient. This is if a patient contact would have more than one value for their Relationship to Patient (I RLA 1000). |
| 4 | `ADDL_REL_START_DATE` | DATETIME |  | Indicates the start date of the patient contact's "Additional Relation to Patient" (I RLA 360) item. |
| 5 | `ADDL_REL_END_DATE` | DATETIME |  | Indicates the end date of the patient contact's "Additional Relation to Patient" (I RLA 360) item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

