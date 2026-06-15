# MYC_CONVO_EXPORT_AUDIT

> MyChart conversation export audit.

**Primary key:** `THREAD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `THREAD_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the thread record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SOURCE_ORG_ID` | NUMERIC |  | Stores the DXO record of the organization who exported the message |
| 4 | `SOURCE_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 5 | `EXPORT_UTC_DTTM` | DATETIME (UTC) |  | It stores the export instant in UTC. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `THREAD_ID` | [MYC_CONVO](MYC_CONVO.md) | sole_pk | high |

