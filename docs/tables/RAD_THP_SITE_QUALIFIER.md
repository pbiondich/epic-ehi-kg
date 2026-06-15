# RAD_THP_SITE_QUALIFIER

> THE RAD_THP_SITE_QUALIFIERS table contains further information regarding the location of treatment during radiation therapy. These location qualifiers provide greater detail about the body site found in RAD_THP_SITE_AND_TECHNIQUE and can be used to more precisely describe the treatment location.

**Primary key:** `SUMMARY_BLOCK_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `RAD_THP_SITE_QUALIFIER_C_NAME` | VARCHAR |  | The category ID of a location qualifier for a body site being treated as part of this radiation therapy episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

