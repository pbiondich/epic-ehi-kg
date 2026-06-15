# HNO_PLAIN_TEXT

> This table extracts notes that are stored only in plain text. This table does not contain any notes that are stored in rich text. HNO_NOTE_TEXT should still be used for reporting purposes.

**Primary key:** `NOTE_CSN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_CSN_ID` | NUMERIC | PK FK→ | The contact serial number (CSN) of the contact. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `NOTE_ID` | VARCHAR | shared | The unique identifier (.1 item) for the note record. |
| 4 | `NOTE_TEXT` | VARCHAR |  | Content of the plain text note. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NOTE_CSN_ID` | [NOTE_ENC_INFO](NOTE_ENC_INFO.md) | overflow_master | medium |

