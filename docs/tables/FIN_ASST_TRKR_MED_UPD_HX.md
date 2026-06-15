# FIN_ASST_TRKR_MED_UPD_HX

> This table contains a history of the edits made to the list of medications attached to a medication assistance program tracker.

**Primary key:** `FIN_ASST_TRACKER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_TRACKER_ID` | NUMERIC | PK FK→ | The unique identifier for the program tracker record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated update for the tracker. Along with FIN_ASST_TRACKER_ID, this forms the foreign key link to the FIN_ASST_TRKR_UPDATE_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple medication lines associated with the tracker and update from the FIN_ASST_TRKR_UPDATE_HX table. |
| 4 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_TRACKER_ID` | [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | name_stem | high |

