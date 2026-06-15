# OR_CASE_VIRTUAL

> The OR_CASE_VIRTUAL table contains virtual items for the OR management system case records.

**Primary key:** `OR_CASE_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique identifier for the case request record. |
| 2 | `ADD_ON_CASE_SCH_YN` | VARCHAR |  | Indicates whether a case has been added-on to the schedule after the schedule was finalized for the day, as defined by settings specified on Scheduling 2 node in System and Location Definitions (not the add-on checkbox in the case). Y indicates that the case was added-on after the time the schedule was finalized. N indicates that the case was not added-on after the time the schedule was finalized. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

