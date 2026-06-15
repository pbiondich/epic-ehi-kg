# PAT_REL_ROLES_EPSD

> This table contains patient contact roles towards the patient for episode-level relationships. The records included in this table are Patient Relationships (RLA) records.

**Primary key:** `PAT_RELATIONSHIP_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_RELATIONSHIP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient contact record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the episode information in the patient contact. Together with PAT_RELATIONSHIP_ID, this forms the foreign key to the PAT_REL_INFO_EPSD and the PAT_REL_NOTES_EPSD tables. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of multiple roles associated with the patient contact and episode from the PAT_REL_INFO_EPSD table. |
| 4 | `EPSD_ROLE_TO_PAT_C_NAME` | VARCHAR | org | The role category ID of the patient contact at the episode-level. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_RELATIONSHIP_ID` | [PAT_RELATIONSHIP_LIST](PAT_RELATIONSHIP_LIST.md) | sole_pk | high |

