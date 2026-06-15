# BND_EPSD_EXCL_VISITS

> This table stores the list of patient contacts that should not be billed as part of a bundled episode.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the bundled episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VISIT_CSN` | NUMERIC |  | The contact serial number of the patient contact that should not be billed as part of the bundled episode. |
| 4 | `BND_EPSD_VISIT_SRC_C_NAME` | VARCHAR |  | This column stores the category ID of the source that indicated that the associated visit should not be billed as part of the bundled episode. |
| 5 | `VISIT_UPDATE_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user who last associated the visit that should not be billed as part of the bundled episode. |
| 6 | `VISIT_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `VISIT_UPDATE_DTTM` | DATETIME (UTC) |  | The date and time that the user last associated the visit that should not be billed as part of the bundled episode. |
| 8 | `DEFINES_CLIN_LINK_YN` | VARCHAR |  | Indicates whether the billing unlink is the reason the episode is unlinked on the clinical side (i.e. it hasn't ever been linked or unlinked directly from the clinical side). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

