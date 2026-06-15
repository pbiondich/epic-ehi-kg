# PAT_REL_NOTES_EPSD

> This table contains the IDs of notes about episode-level relationships. The records included in this table are Patient Relationships (RLA) records.

**Primary key:** `PAT_RELATIONSHIP_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_RELATIONSHIP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient contact record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the episode information in the patient contact. Together with PAT_RELATIONSHIP_ID, this forms the foreign key to the PAT_REL_INFO_EPSD and the PAT_REL_NOTES_EPSD tables. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of multiple notes associated with the patient contact and episode from the PAT_REL_INFO_EPSD table. |
| 4 | `EPSD_NOTE_ID` | VARCHAR |  | The unique ID of episode-level note for a patient contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_RELATIONSHIP_ID` | [PAT_RELATIONSHIP_LIST](PAT_RELATIONSHIP_LIST.md) | sole_pk | high |

