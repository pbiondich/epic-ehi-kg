# REFERRAL_NOTES

> Notes attached to the referral record.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTE_ID` | VARCHAR | shared | The unique identifier for the note record. |
| 4 | `NOTE_USER_ID` | VARCHAR |  | User who created the note. |
| 5 | `NOTE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `NOTE_DATETIME` | DATETIME (Attached) |  | The instant of creation of the note. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

