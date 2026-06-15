# ACCT_NOTEPAD

> This table contains information about the account notes.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACCT_NOTE_TEXT` | VARCHAR |  | The text of the account note. This contains the first 4000 characters of the text line. |
| 4 | `ACCT_NOTE_TEXT_2` | VARCHAR |  | The text of the account note. This contains characters 4001 to 8000. |
| 5 | `ACCT_NOTE_TEXT_3` | VARCHAR |  | The text of the account note. This contains characters 8001 to 12000. |
| 6 | `ACCT_NOTE_TEXT_4` | VARCHAR |  | The text of the account note. This contains characters 12001 to 16000. |
| 7 | `ACCT_NOTE_TEXT_5` | VARCHAR |  | The text of the account note. This contains characters 16001 to 20000. |
| 8 | `ACCT_NOTE_TEXT_6` | VARCHAR |  | The text of the account note. This contains characters 20001 to 24000. |
| 9 | `ACCT_NOTE_TEXT_7` | VARCHAR |  | The text of the account note. This contains characters 24001 to 28000. |
| 10 | `ACCT_NOTE_TEXT_8` | VARCHAR |  | The text of the account note. This contains characters 28001 to 32000. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

