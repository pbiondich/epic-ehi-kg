# LETTER_PRINT_AUDIT

> Shows an audit of letter printing in Customer Relationship Management records.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier of the communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTE_CSN_ID` | NUMERIC | FK→ | The contact serial number (CSN) of a printed letter. |
| 4 | `PRINT_DATETIME` | DATETIME (UTC) |  | The date and time when the letter was printed in UTC format. |
| 5 | `USER_ID` | VARCHAR | FK→ | Stores the ID of the user who printed the letter |
| 6 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NOTE_CSN_ID` | [NOTE_ENC_INFO](NOTE_ENC_INFO.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

