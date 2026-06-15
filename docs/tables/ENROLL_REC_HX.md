# ENROLL_REC_HX

> The ENROLL_REC_HX table contains a history of patient enrollment deletions and undeletions.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique ID of the patient enrollment record for this row. This column is frequently used to link to the ENROLL_INFO table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SDFL_EDIT_INSTANT` | DATETIME (Local) |  | The instant that the record status was changed |
| 4 | `SDFL_EDIT_USER_ID` | VARCHAR |  | The user who changed the record status |
| 5 | `SDFL_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `SDFL_EDIT_ACTION_C_NAME` | VARCHAR |  | The action that was applied to the record status |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

