# DOC_INFO_NOTES

> The DOC_INFO_NOTES table contains notes about documents, including scanned and electronically signed documents.

**Primary key:** `DOC_INFO_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOC_INFO_ID` | VARCHAR | PK FK→ | The unique ID of the document information record. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each row of notes for a document information record. |
| 3 | `DOC_NOTE` | VARCHAR |  | A line of free text containing information of note for this document. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DOC_INFO_ID` | [DOC_INFORMATION](DOC_INFORMATION.md) | sole_pk | high |

