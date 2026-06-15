# ENROLL_STUDY_COORD

> The ENROLL_STUDY_COORD table identifies study coordinators for a patient's enrollment in a research study.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique ID of the patient enrollment record for this row. This column is frequently used to link to the ENROLL_INFO table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STUDY_COORD_ID` | VARCHAR |  | The IDs of study coordinators for a patient enrollment in a study. Chosen from a list of users defined at the Research Study level. |
| 4 | `STUDY_COORD_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

