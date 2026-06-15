# COMMUNICATION_PREFERENCES

> Contains communication concepts and preferred media.

**Primary key:** `PREFERENCES_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PREFERENCES_ID` | NUMERIC | PK FK→ | The internal ID of the preference record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMMUNICATION_CONCEPT_ID` | NUMERIC |  | The unique ID of the communication concept (HST) record. Communication preferences will be stored for each concept. |
| 4 | `COMMUNICATION_CONCEPT_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PREFERENCES_ID` | [COMM_PREF_ADDL_ITEMS](COMM_PREF_ADDL_ITEMS.md) | sole_pk | high |

