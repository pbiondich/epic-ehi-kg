# CARE_TEAM_PROV_STATUS

> Stores data about patient's care team provider stautses.

**Primary key:** `MYPT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MYPT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the patient record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CT_PAT_ID` | VARCHAR | FK→ | The ID of the patient that has the provider on their care team. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CT_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

