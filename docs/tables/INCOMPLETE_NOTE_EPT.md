# INCOMPLETE_NOTE_EPT

> Table created for the visit narrative data stored in the patient masterfile. No longer used since we use UCN now since 2010, exporting these items as a formality.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `INC_NOTE_USER_ID` | VARCHAR |  | The user ID for an incomplete note, not used since 2010 and only exported as a formality. |
| 7 | `INC_NOTE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `INC_NOTE_NOTE_ID` | VARCHAR |  | The note ID for an incomplete note, not used since 2010 and only exported as a formality. |
| 9 | `INC_NOTE_TYPE_C_NAME` | VARCHAR | org | The note type for an incomplete note, not used since 2010 and only exported as a formality. |
| 10 | `INC_NOTE_MSG_ID` | VARCHAR |  | The inbasket message ID for an incomplete note, not used since 2010 and only exported as a formality. |
| 11 | `INC_NOTE_START_DATE_UTC_DTTM` | DATETIME (UTC) |  | The start date for an incomplete note, not used since 2010 and only exported as a formality. |
| 12 | `INC_NOTE_LAST_EDIT_UTC_DTTM` | DATETIME (UTC) |  | The end date for an incomplete note, not used since 2010 and only exported as a formality. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

