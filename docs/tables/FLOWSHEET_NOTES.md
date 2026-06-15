# FLOWSHEET_NOTES

> This table displays notes that are linked to flowsheet data.

**Primary key:** `FSD_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FSD_ID` | VARCHAR | PK FK→ | The flowsheet data ID. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the flowsheet data record that corresponds to this specific data. |
| 3 | `VALUE_LINE` | INTEGER | PK | The value line of the flowsheet notes item. |
| 4 | `LINKED_NOTES_ID` | VARCHAR |  | Stores the note record ID's of notes that are associated with this data through the flowsheet notes functionality. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FSD_ID` | [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | sole_pk | high |

