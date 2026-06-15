# SEP1_AUTOPOP_SEPSIS_DOC

> This table contains autopopulation data source information for the earliest physician, APN or PA documentation of sepsis for the CMS SEP-1 core measure.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTE_ID` | VARCHAR | shared | The ID of the note that contains the earliest physician, APN, or PA documentation of sepsis. |
| 4 | `NOTE_CSN_ID` | NUMERIC | FK→ | The contact serial number (CSN) of the note that contains earliest physician, APN, or PA documentation of sepsis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NOTE_CSN_ID` | [NOTE_ENC_INFO](NOTE_ENC_INFO.md) | overflow_master | medium |

