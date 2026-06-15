# FAMILY_PATS_LINKED_EPSDS

> The FAMILY_PATS_LINKED_EPSDS table contains information about the episodes linked to a particular family member within a family.

**Primary key:** `FAMILY_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FAMILY_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the family record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the patient in the family. Together with FAMILY_ID, this forms the foreign key to the FAMILY_PATS table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple linked episodes associated with the family and the patient from the FAMILY_PATS table. |
| 4 | `LINKED_EPISODE_ID` | NUMERIC |  | The unique ID of the episode linked to this family member. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FAMILY_ID` | [FAMILY](FAMILY.md) | sole_pk | high |

