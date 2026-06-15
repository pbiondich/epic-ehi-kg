# NOTES_ACCT

> This table contains summary information for billing system account notepad notes attached to accounts.

**Primary key:** `NOTE_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique ID of the Account Notepad note record. |
| 2 | `ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the guarantor associated with the note. It is only populated for guarantor-level notes. |
| 3 | `ACTIVE_STATUS` | VARCHAR |  | The status of the note: active or inactive. |
| 4 | `ENTRY_USER_ID` | VARCHAR |  | The ID of the user who manually created the note. If the note was automatically created by billing system, this is the person who executed the activity that triggered the note creation. This ID may be encrypted |
| 5 | `ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `INVOICE_NUMBER` | VARCHAR |  | The invoice number associated with this note. |
| 7 | `NOTE_ENTRY_DTTM` | DATETIME (Local) |  | The date and time the account note was created. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

