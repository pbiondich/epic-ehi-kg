# EPSD_FILED_SF

> This table contains the IDs of SmartForms which have been filed for each episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier of the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `FILED_SF_ID` | VARCHAR |  | The IDs of the SmartForms that have been filed for this episode. |
| 4 | `FILED_SF_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

