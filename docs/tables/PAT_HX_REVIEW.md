# PAT_HX_REVIEW

> This table contains information about when a patient's history was reviewed and by whom. More detailed information on what kinds of history were reviewed is in the PAT_HX_REV_TYPE and PAT_HX_REV_TOPIC tables.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE_COUNT`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE_COUNT` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `HX_REVIEWED_USER_ID` | VARCHAR |  | The unique ID of the user who reviewed history for the patient. |
| 5 | `HX_REVIEWED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `HX_REVIEWED_DATE` | DATETIME |  | The date history was reviewed for this patient. |
| 7 | `HX_REVIEWED_INSTANT` | DATETIME (Local) |  | The date and time history was reviewed for this patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

