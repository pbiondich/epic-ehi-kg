# COMM_PREFERENCES_APRV

> This table extracts the related multiple response item OYO-104, which contains the media approved for use by a person for a given communication concept.

**Primary key:** `PREFERENCES_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PREFERENCES_ID` | NUMERIC | PK FK→ | The internal ID of the preference record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `APRV_MEDIA_C_NAME` | VARCHAR |  | The approved communication media for a communication concept. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PREFERENCES_ID` | [COMM_PREF_ADDL_ITEMS](COMM_PREF_ADDL_ITEMS.md) | sole_pk | high |

