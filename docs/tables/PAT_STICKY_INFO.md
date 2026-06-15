# PAT_STICKY_INFO

> The PAT_STICKY_INFO table contains information of patient's sticky note, including user ID whom the sticky note belongs to and note ID which the sticky note is stored in.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STICKY_USER_ID` | VARCHAR |  | User ID whom the sticky note belongs to. |
| 4 | `STICKY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `STICKY_NOTE_ID` | VARCHAR |  | Note ID which the sticky note is stored in. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

