# V_EHI_PBA_NOTES_MC_PBA

> This view filters out account data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `NOTE_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier of a note attached to the account. |
| 2 | `NOTE_DATE` | DATETIME |  | The date when the note was created. This column contains date information only. Column NOTE_DATETIME holds date and time information. |
| 3 | `NOTE_USER_ID` | VARCHAR |  | The unique identifier of the user that created the note. |
| 4 | `NOTE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `PB_ACCT_ID` | VARCHAR | FK→ | The unique identifier of the Premium Billing account. |
| 6 | `NOTE_LOCAL_DTTM` | DATETIME (Local) |  | The date and time the note was created. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |

