# PAT_SOCIAL_HX_DOC

> This table contains the history documentation related to your patients for an encounter. Each row represents one line of history documentation text for a given encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique identifier of the patient encounter. Contact serial number is unique across all patients and all contacts. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_SOCIAL_DOC` | VARCHAR |  | Contents of the Social Documentation section of the patient's History activity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

