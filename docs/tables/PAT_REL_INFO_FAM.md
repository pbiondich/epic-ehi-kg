# PAT_REL_INFO_FAM

> Contains information about a patient's relationship specific to a particular family.

**Primary key:** `PAT_RELATIONSHIP_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_RELATIONSHIP_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the relationship record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FAMILY_ID` | NUMERIC | FK→ | Stores the id of the family associated with this relationship |
| 4 | `FAMILY_NOTE_ID` | VARCHAR |  | Stores a note associated with a relationship within a family. This note can be shared between 2 RLAs related to the 2 patients in the relationship. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FAMILY_ID` | [FAMILY](FAMILY.md) | sole_pk | high |
| `PAT_RELATIONSHIP_ID` | [PAT_RELATIONSHIP_LIST](PAT_RELATIONSHIP_LIST.md) | sole_pk | high |

