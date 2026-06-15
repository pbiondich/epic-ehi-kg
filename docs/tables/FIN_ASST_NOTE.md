# FIN_ASST_NOTE

> This table contains information about notes added to financial assistance tracker records.

**Primary key:** `NOTE_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `HNO_RECORD_TYPE_C_NAME` | VARCHAR |  | Record type. |
| 3 | `ENTRY_PERSON_USER_ID` | VARCHAR |  | Note Entry Person |
| 4 | `ENTRY_PERSON_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ENTRY_DATE` | DATETIME |  | The date on which this note was created. |
| 6 | `ACCT_NOTE_INSTANT_DTTM` | DATETIME (Local) |  | The instant in which this note was created. |
| 7 | `ACCT_NOTE_SUMMARY` | VARCHAR |  | A brief summary of the content of this note to aid in note identification. |
| 8 | `SYSTEM_GEN_YN` | VARCHAR |  | Denotes whether a financial assistance note was generated automatically by the system. |
| 9 | `FIN_ASST_CASE_ID` | NUMERIC | FK→ | This item stores the internal ID of the financial assistance case record this note is linked to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

