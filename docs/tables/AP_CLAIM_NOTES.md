# AP_CLAIM_NOTES

> The AP_CLAIM_NOTES table contains information about the notes that are attached to each claim.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim to which the note is attached. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTE_ID` | VARCHAR | shared | Note identifier. Can be used to join to tables such as HNO_INFO and NOTE_ENC_INFO. |
| 4 | `NOTE_DTTM` | DATETIME (Local) |  | The date and time the note was created. |
| 5 | `NOTE_USER_ID` | VARCHAR |  | The unique ID of the user who created the note associated with the claim record. |
| 6 | `NOTE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

