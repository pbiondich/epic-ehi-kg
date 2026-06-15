# OPH_EXAM_DATA

> Stores ophthalmology exam information documented in the visit.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `OPHTH_BUVA_OD` | NUMERIC |  | Stores the best uncorrected visual acuity in logMAR notation for the right eye within the visit. |
| 4 | `OPHTH_BCVA_OD` | NUMERIC |  | Stores the best corrected visual acuity in logMAR notation for the right eye within the visit. |
| 5 | `OPHTH_BUVA_OS` | NUMERIC |  | Stores the best uncorrected visual acuity in logMAR notation for the left eye within the visit. |
| 6 | `OPHTH_BCVA_OS` | NUMERIC |  | Stores the best corrected visual acuity in logMAR notation for the left eye within the visit. |
| 7 | `OPHTH_BUVA_DISP_OD` | VARCHAR |  | Stores the entered display format for the best visual acuity at distance uncorrected for the right eye. |
| 8 | `OPHTH_BCVA_DISP_OD` | VARCHAR |  | Stores the entered display format for the best visual acuity at distance corrected for the right eye. |
| 9 | `OPHTH_BUVA_DISP_OS` | VARCHAR |  | Stores the entered display format for the best visual acuity at distance uncorrected for the left eye. |
| 10 | `OPHTH_BCVA_DISP_OS` | VARCHAR |  | Stores the entered display format for the best visual acuity at distance corrected for the left eye. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

