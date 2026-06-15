# CARE_COORDINATION

> This table will contain data relevant to the Ambulatory patient Care Coordination. Currently this is just the Care Coordination note.

**Primary key:** `PAT_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting's encryption utility. |
| 2 | `CARE_COORD_NOTE_ID` | VARCHAR |  | Stores the ID of the Care Coordination note. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

