# SDD_ENTRIES

> This table stores basic info about Social Driver entries. Each row represents one documentation of a need or risk for the patient in a given domain. This data includes the score that defines the severity of this need or risk.

**Primary key:** `SDOH_DATA_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SDOH_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the social driver data record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ENTRY_DOM_CONFIG_ID_RECORD_NAME` | VARCHAR |  | The name of the social driver domain configuration record. |
| 6 | `ENTRY_EFFECTIVE_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant at which an entry in SDD was considered active. |
| 7 | `ENTRY_CONCERN_LVL_C_NAME` | VARCHAR |  | Stores the level of concern for this entry on a scale of low, medium, or high (or unknown). |
| 8 | `ENTRY_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the CSN of the encounter where this entry was filed |
| 9 | `ENTRY_USER_ID` | VARCHAR |  | Stores the user who documented this entry |
| 10 | `ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `ENTRY_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENTRY_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `SDOH_DATA_ID` | [SDD_DATA](SDD_DATA.md) | sole_pk | high |

