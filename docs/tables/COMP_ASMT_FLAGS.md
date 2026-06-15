# COMP_ASMT_FLAGS

> This table contains information about flags that were added to the hospice comprehensive assessment. Comprehensive assessment flags are used to highlight important or unusual information on a specific form in the comprehensive assessment.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FLAG_TYPE_C_NAME` | VARCHAR | org | This item stores the flag type for flags added to the comprehensive assessment. |
| 4 | `FLAG_ENCOUNTER_CSN` | NUMERIC |  | This item stores a link to the patient contact in which this flag was added. |
| 5 | `FLAG_COMMENTS` | VARCHAR |  | This item stores free text comments associated with a flag attached to a comprehensive assessment. |
| 6 | `CREATED_BY_USER_ID` | VARCHAR |  | The user record ID of the user that created this flag. |
| 7 | `CREATED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `CREATED_ON_DTTM` | DATETIME (UTC) |  | This item stores the instant at which the flag was created and added to the comprehensive assessment. |
| 9 | `CLEARED_BY_USER_ID` | VARCHAR |  | The user record ID of the user who cleared or removed the flag from the comprehensive assessment. |
| 10 | `CLEARED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `CLEARED_ON_DTTM` | DATETIME (UTC) |  | The instant at which this flag was cleared or removed from the comprehensive assessment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

