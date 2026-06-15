# NOTE_SMARTBLOCK_ATTR

> Store the employee (EMP) ID, the Timestamp, and the SmartBlocks added of the Attribution for SmartBlocks.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `USER_ID` | VARCHAR | FK→ | This item stores the unique ID of the user part of the attribution for SmartBlocks (forms that generate text for a note) |
| 4 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ATTRIBUTION_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant part of the attribution for SmartBlocks (forms that generate text for a note). |
| 6 | `SB_COPY_CSN` | NUMERIC |  | Stores the contact serial number (CSN) of the note from which this attributed data was copied. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

