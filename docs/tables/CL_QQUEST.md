# CL_QQUEST

> The CL_QQUEST table is the primary table for storing non-contact specific information related to questions in a questionnaire.

**Primary key:** `QUEST_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `QUEST_ID` | VARCHAR | PK | The unique ID of the question record. |
| 2 | `QUEST_NAME` | VARCHAR |  | The name of the question record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [CL_QQUEST_OVTM](CL_QQUEST_OVTM.md) | `QUEST_ID` | high |

