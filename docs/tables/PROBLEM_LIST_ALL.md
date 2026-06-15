# PROBLEM_LIST_ALL

> This is a generic table that contains every Problem List (LPL) record regardless of its type. It also contains a link to the patient record that is associated with the LPL record, a column indicating the type of LPL record, and an optional link from a Problem History record (type 7) to the corresponding Problem record (type 1) that it describes.

**Primary key:** `PROBLEM_LIST_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the problem record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record associated with this problem list. |
| 3 | `HX_SOURCE_ID` | NUMERIC |  | Stores the ID of the problem record that this history record describes. |
| 4 | `RECORD_TYPE_C_NAME` | VARCHAR |  | Indicates the type of information stored in this record, such as Problem List, Allergy, Immunization, etc. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

