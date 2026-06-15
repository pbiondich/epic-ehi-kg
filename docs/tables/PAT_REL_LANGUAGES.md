# PAT_REL_LANGUAGES

> This table contains information about the patient contacts' languages. The records included in this table are Patient Relationships (RLA) records.

**Primary key:** `PAT_RELATIONSHIP_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_RELATIONSHIP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient contact record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LANGUAGE_C_NAME` | VARCHAR | org | The language category ID for the patient contact. |
| 4 | `LANGUAGE_TYPE_C_NAME` | VARCHAR |  | The language type category ID for the patient contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_RELATIONSHIP_ID` | [PAT_RELATIONSHIP_LIST](PAT_RELATIONSHIP_LIST.md) | sole_pk | high |

