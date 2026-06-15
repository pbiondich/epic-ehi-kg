# NOTE_EXT_SIGNERS

> Note signer information for auto-reconciled external notes.

**Primary key:** `NOTE_CSN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_CSN_ID` | NUMERIC | PK FK→ | The contact serial number (CSN) of the contact. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `NOTE_ID` | VARCHAR | shared | The unique identifier (.1 item) for the note record. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `EXT_NOTE_SIGNER_NAME` | VARCHAR |  | An auto-reconciled external note signer's name. |
| 6 | `EXT_NOTE_SIGNING_UTC_DTTM` | DATETIME (UTC) |  | An auto-reconciled external note signing instant for a note signer. |
| 7 | `EXT_NOTE_SIGNER_ROLE_C_NAME` | VARCHAR |  | External note signer's role in authenticating the content of an auto-reconciled external note. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NOTE_CSN_ID` | [NOTE_ENC_INFO](NOTE_ENC_INFO.md) | overflow_master | medium |

