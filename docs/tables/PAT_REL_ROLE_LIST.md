# PAT_REL_ROLE_LIST

> This table contains patient contacts' role(s) in relation to the patient. It includes the patient contact's role, the date the role started, and the date the role ended. The records included in this table are Patient Relationships (RLA) records.

**Primary key:** `RELATIONSHIP_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RELATIONSHIP_ID` | NUMERIC | PK | The unique identifier for the patient contact record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ROLE_C_NAME` | VARCHAR | org | The role category ID of the patient contact at the patient-level. |
| 4 | `ROLE_START_DATE` | DATETIME |  | The date when the patient contact's role starts. |
| 5 | `ROLE_END_DATE` | DATETIME |  | The date when the patient contact's role ends. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

