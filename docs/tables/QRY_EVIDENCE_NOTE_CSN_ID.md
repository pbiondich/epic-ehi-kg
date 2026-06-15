# QRY_EVIDENCE_NOTE_CSN_ID

> This table extracts information related to the contact the evidence came from.

**Primary key:** `QUERY_CSN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `QUERY_ID` | NUMERIC | FK→ | The unique identifier for the query record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `EVIDENCE_NOTE_CSN_ID` | NUMERIC |  | The unique ID of the contact of the note record that contains this evidence. |
| 6 | `QUERY_CSN_ID` | NUMERIC | PK FK→ | The contact serial number (CSN) of the contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `QUERY_CSN_ID` | [QRY_CONTACT_INFO](QRY_CONTACT_INFO.md) | sole_pk | high |
| `QUERY_ID` | [QRY_RECORD_INFO](QRY_RECORD_INFO.md) | sole_pk | high |

