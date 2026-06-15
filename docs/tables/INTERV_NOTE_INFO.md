# INTERV_NOTE_INFO

> This table links a care plan goal note contact to the related intervention note contacts that were filed at the same time.

**Primary key:** `NOTE_CSN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number (CSN) of the goal note contact. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `NOTE_ID` | VARCHAR | shared | The unique identifier for the goal note record. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `INTERV_NOTE_CSN_ID` | NUMERIC |  | The unique contact serial number for one of the child intervention notes that was documented at the same time as this goal note. A goal note links to the contact serial numbers of all of the child intervention notes that were filed at the same time as the goal note so that this related documentation can be shown together. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NOTE_CSN_ID` | [NOTE_ENC_INFO](NOTE_ENC_INFO.md) | overflow_master | medium |

