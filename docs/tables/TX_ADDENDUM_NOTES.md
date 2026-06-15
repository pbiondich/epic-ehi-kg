# TX_ADDENDUM_NOTES

> Extract Note (HNO) records containing addendum information for the note.

**Primary key:** `NOTE_CSN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number (CSN) of the note record. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `NOTE_ID` | VARCHAR | shared | The unique identifier (.1 item) for the note record. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `TX_ADDENDUM_NOTE_ID` | VARCHAR |  | Legacy item used to identify related note records containing addendum information for the note. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NOTE_CSN_ID` | [NOTE_ENC_INFO](NOTE_ENC_INFO.md) | overflow_master | medium |

