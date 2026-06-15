# GROUP_FACILITATORS

> A table describing the facilitators for a group.

**Primary key:** `PAT_GROUP_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_GROUP_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the group record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GROUP_FACILITATORS_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_GROUP_ID` | [PAT_GROUP](PAT_GROUP.md) | sole_pk | high |

