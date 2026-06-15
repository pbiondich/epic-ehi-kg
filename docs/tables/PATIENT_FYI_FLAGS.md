# PATIENT_FYI_FLAGS

> This table will extract Patient FYI flags from the Notes (HNO) database. These are notes with a Patient Flag Type (I HNO 560) that is not null.

**Primary key:** `NOTE_ID`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier of the note (HNO) |
| 2 | `DELETED_CAT_C_NAME` | VARCHAR |  | Indicates the Deleted Status of this Note record in Chronicles. |
| 3 | `ACTIVE_C_NAME` | VARCHAR |  | Indicates if this Patient FYI Flag will be shown as an Active or Inactive flag. |
| 4 | `ENTRY_PERSON_ID` | VARCHAR |  | The unique identifier of the user (EMP) who created this Patient FYI Flag. |
| 5 | `ENTRY_PERSON_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `ACCT_NOTE_INSTANT` | DATETIME (Local) |  | The instant at which this FYI flag was created. |
| 7 | `ACCT_NOTE_SUMMARY` | VARCHAR |  | The brief free text summary statement about the Patient FYI. |
| 8 | `PAT_FLAG_TYPE_C_NAME` | VARCHAR | org | The type of Patient FYI Flag. This is a customer owned list. |
| 9 | `PT_FG_PURGABLE_YN` | VARCHAR |  | Indicates whether a batch can purge this patient flag. A Y indicates the flag can be purged. N indicates the flag cannot be purged. |
| 10 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The Patient Encounter this Patient FYI is associated with. This field may be null, if the FYI is at the patient level rather than contact specific. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

