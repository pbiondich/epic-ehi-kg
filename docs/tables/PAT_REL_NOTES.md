# PAT_REL_NOTES

> This table contains the IDs of notes about patient-level relationships. The records included in this table are Patient Relationships (RLA) records.

**Primary key:** `PAT_RELATIONSHIP_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_RELATIONSHIP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient contact record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTE_ID` | VARCHAR | shared | The unique ID of the patient-level note for a patient contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_RELATIONSHIP_ID` | [PAT_RELATIONSHIP_LIST](PAT_RELATIONSHIP_LIST.md) | sole_pk | high |

