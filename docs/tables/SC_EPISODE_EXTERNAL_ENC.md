# SC_EPISODE_EXTERNAL_ENC

> Data about external encounters linked to a Compass Rose episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REFERENCE` | VARCHAR |  | The composite DXR reference ID for an external encounter linked to this episode. |
| 4 | `METRIC_STATUS_C_NAME` | VARCHAR |  | The status category ID for an external encounter linked to this episode. |
| 5 | `BND_EPSD_SRC_C_NAME` | VARCHAR |  | The source category ID for an external encounter linked to this episode. |
| 6 | `INVALIDATION_DATE` | DATETIME |  | The date when the link was found to be invalid for an external encounter linked to this episode. |
| 7 | `START_DTTM` | DATETIME (Local) |  | The encounter start date and time for an external encounter linked to this episode. This will only be populated for non-Epic encounters and is used to match an encounter to an existing link even when the reference ID changes. |
| 8 | `END_DTTM` | DATETIME (Local) |  | The encounter end date and time for an external encounter linked to this episode. This will only be populated for non-Epic encounters and is used to match an encounter to an existing link even when the reference ID changes. |
| 9 | `DISP_ENC_TYPE_C_NAME` | VARCHAR | org | The encounter type category ID for an external encounter linked to this episode. This will only be populated for non-Epic encounters and is used to match an encounter to an existing link even when the reference ID changes. |
| 10 | `ENC_TYPE_NAME` | VARCHAR |  | The encounter type free text name for an external encounter linked to this episode. This will only be populated for non-Epic encounters and is used to match an encounter to an existing link even when the reference ID changes. |
| 11 | `ORG_ID` | NUMERIC |  | A unique organization identifier that consists of the name and the organization ID for the source organization of an external encounter linked to this episode. This column is often used for grouping, sorting, and display purposes in reports. |
| 12 | `ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

