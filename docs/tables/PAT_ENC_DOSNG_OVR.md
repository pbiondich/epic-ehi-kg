# PAT_ENC_DOSNG_OVR

> The PAT_ENC_DOSNG_OVR table contains the dosing instructions for individual days (such as holds, changes to doses for a day, missed doses, wrong doses taken) for anticoagulation patients when using the calendar based tracking section.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `OVERRIDE_DATE` | DATETIME |  | Date for which a daily correction is specified (may be a held dose, dose change to instructions, missed dose, wrong dose taken or comment) |
| 7 | `OVERRIDE_DOSE` | NUMERIC |  | Override dose for the day (dose change or wrong dose taken) |
| 8 | `OVERRIDE_PILL_SIZE` | VARCHAR |  | Override pill size for the day (dose change) |
| 9 | `OVERRIDE_NO_OF_PILL` | NUMERIC |  | Override number of pills for the day (dose change) |
| 10 | `HOLD_DOSE_YN` | VARCHAR |  | This column will store a boolean Yes/No about whether the patient was instructed to hold their dose for the day. |
| 11 | `OVERRIDE_COMMENTS` | VARCHAR |  | Override comments for the day |
| 12 | `DOSE_MISSED_YN` | VARCHAR |  | This column will store a boolean Yes/No about whether the patient missed their dose for the day. |
| 13 | `UNDO_CORRECTION_YN` | VARCHAR |  | This item will be used to undo the correction day. Setting this item to Yes will ignore this correction from being displayed on calendar. |
| 14 | `WRONG_DOSE_TAKEN_YN` | VARCHAR |  | This item will store a boolean Yes/No about whether the patient took the wrong dose |
| 15 | `OVERRIDE_PILL_SIZE2` | VARCHAR |  | Second override pill size for the day (dose change) |
| 16 | `OVERRIDE_NO_OF_PIL2` | NUMERIC |  | Second override number of pills for the day (dose change) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

