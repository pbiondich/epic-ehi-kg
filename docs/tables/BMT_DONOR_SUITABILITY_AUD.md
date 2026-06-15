# BMT_DONOR_SUITABILITY_AUD

> Audit history information for BMT donor selection, suitability, and availability information.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SUITABILITY_C_NAME` | VARCHAR |  | Donor suitability audit item |
| 4 | `AVAILABILITY_C_NAME` | VARCHAR |  | Donor availability audit item |
| 5 | `SELECTION_C_NAME` | VARCHAR |  | Donor selection audit item |
| 6 | `UPDATE_USER_ID` | VARCHAR |  | Donor suitability and selection audit user |
| 7 | `UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `START_UTC_DTTM` | DATETIME (UTC) |  | Donor suitability and selection audit instant |
| 9 | `END_UTC_DTTM` | DATETIME (UTC) |  | The end instant for a given set of donor suitability, availability, and selection values |
| 10 | `DNR_WRKP_AUD_C_NAME` | VARCHAR |  | Donor workup audit item |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

