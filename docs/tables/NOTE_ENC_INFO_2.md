# NOTE_ENC_INFO_2

> This table extends HNO_ENC_INFO.

**Overflow of:** [NOTE_ENC_INFO](NOTE_ENC_INFO.md)  
**Primary key:** `NOTE_CSN_ID`  
**Columns:** 14  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_CSN_ID` | NUMERIC | PK | The contact serial number (CSN) of the contact. |
| 2 | `NOTE_ID` | VARCHAR | shared | The unique identifier (.1 item) for the note record. |
| 3 | `CONTACT_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CONTACT_NUM` | VARCHAR |  | Contact number |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `EXT_SHARED_W_PT_YN` | VARCHAR |  | Autoreconciled external note share with patient status |
| 8 | `EXT_AUTH_NAME` | VARCHAR |  | Autoreconciled external note author free text name |
| 9 | `EXT_AUTH_SPEC_C_NAME` | VARCHAR | org | Autoreconciled external note author specialty |
| 10 | `EXT_AUTH_TYPE` | VARCHAR |  | Autoreconciled external note author type |
| 11 | `EXT_AUTH_SERV` | VARCHAR |  | Autoreconciled external note author service text |
| 12 | `EXT_LAST_SIGNER` | VARCHAR |  | (DEPRECATED) The column EXT_NOTE_SIGNER_NAME[E0000000000443DBD2742EBE5C1C92EA0] in table NOTE_EXT_SIGNERS [E0000000000443DB52742EBE5C1C92EA0] should be used instead. Autoreconciled external note last signer name. |
| 13 | `EXT_LAST_SIGN_UTC_DTTM` | DATETIME (UTC) |  | (DEPRECATED) The column EXT_NOTE_SIGNING_UTC_DTTM [E0000000000443DBE2742EBE5C1C92EA0] in table NOTE_EXT_SIGNERS [E0000000000443DB52742EBE5C1C92EA0] should be used instead. External note signer instant. |
| 14 | `NOTE_AUTHOR_TYPE_C_NAME` | VARCHAR | org | The internal provider type of a note's author, mapped from the transmitted NUCC code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [NOTE_ENC_INFO](NOTE_ENC_INFO.md).

