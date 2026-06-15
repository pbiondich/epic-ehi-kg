# ED_DISPO_AUDIT

> Each record in the ED_DISPO_AUDIT table corresponds to a patient's edited ED disposition. This may not reflect the current values of the disposition, as the records correspond to previous versions of ED disposition information. The fields also capture the instant the ED disposition was initially saved and the user who made the initial entry. It links with a unique contact ID to the previous versions of the note.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this edit. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the deployment owner for this contact. |
| 6 | `ED_DISPOSITION_C_NAME` | VARCHAR | org | The ED disposition of the patient. |
| 7 | `NOTE_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this edited note. This number is unique across all notes in your system, and this column is used to link to the NOTES_HISTORY_LOG table. |
| 8 | `USER_ID` | VARCHAR | FK→ | The unique ID associated with the user record who entered this disposition. |
| 9 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `ED_DISP_INST` | DATETIME (Local) |  | The date and time when this ED disposition was filed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NOTE_CSN_ID` | [NOTE_ENC_INFO](NOTE_ENC_INFO.md) | overflow_master | medium |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

