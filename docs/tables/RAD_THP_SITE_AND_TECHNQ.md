# RAD_THP_SITE_AND_TECHNQ

> The RAD_THP_SITE_AND_TECHNQ table contains information about radiation therapy treatment sites and techniques for a radiation therapy episode.This includes the main body structure or site and the laterality as well as the technique being performed at that location. Further details on the location are found in the corresponding table RAD_THP_SITE_QUALIFIERS.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RAD_THP_BODY_SITE_C_NAME` | VARCHAR |  | The category ID for a body site being treated as part of this radiation therapy episode. |
| 4 | `RAD_THP_LATERALITY_C_NAME` | VARCHAR |  | The category ID for the laterality of the radiation therapy body site on this row. |
| 5 | `RAD_THP_TECHNIQUE_C_NAME` | VARCHAR |  | The category ID of the radiation therapy technique being used to treat the body site on this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

