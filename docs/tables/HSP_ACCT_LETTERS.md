# HSP_ACCT_LETTERS

> This table contains information about hospital billing letters.

**Primary key:** `NOTE_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | This column stores the unique identifier for the note record. |
| 2 | `LETTER_SENT_DATE` | DATETIME |  | The date the letter was sent. |
| 3 | `LET_CREATE_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user who created the letter. |
| 4 | `LET_CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the guarantor account that is associated with this letter. This is only populated for letters sent at the guarantor account level. |
| 6 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account that is associated with this letter. This is only populated for letters sent at the hospital account level. |
| 7 | `BUCKET_ID` | NUMERIC | shared | This column stores the unique identifier for the liability bucket that is associated with this letter. This is only populated for letters sent at the liability bucket level. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

