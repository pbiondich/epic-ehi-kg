# HSP_ACCT_NOTES

> This table contains hospital account notes information from the Notes (HNO) master file. The table includes information about guarantor, patient, hospital account, and hospital liability bucket the note is associated with.

**Primary key:** `NOTE_ID`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | This column stores the unique identifier for the note record associated with a hospital account. |
| 2 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account for which the account note was entered. |
| 3 | `NOTE_ENTRY_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user who entered an account note associated with the hospital account. |
| 4 | `NOTE_ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `NOTE_ENTRY_DT_TIME` | DATETIME (Local) |  | The date and time an account note was entered for a hospital account. |
| 6 | `BUCKET_ID` | NUMERIC | shared | Hospital Liability Bucket linked to this note |
| 7 | `HNO_RECORD_TYPE_C_NAME` | VARCHAR |  | Record type. |
| 8 | `HAR_NOTE_ACCOUNT_ID` | NUMERIC |  | This column stores the unique identifier for the guarantor associated with the hospital account. It is only populated for hospital account-level notes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

